# This is a rhythm game designed for the 13PAD NCEA level 3 Acheivement standard
# This program is coded with python 3 and is mainly using the pygame module for its operation
import pygame
import random
from pygame import mixer
from random import choice
from pygame.locals import *


clock = pygame.time.Clock()
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
pygame.display.set_caption('BOP')


# Importing all images used for this program
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
end_font = pygame.font.Font('font/Pixeltype.ttf', 80)


screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('image/background_1.png').convert_alpha()
background = pygame.transform.scale(background, (800, 600))

start_bg = pygame.image.load('image/start_bg.png').convert_alpha()
start_bg = pygame.transform.scale(start_bg, (800, 600))

start = pygame.image.load('image/start.png').convert_alpha()
start = pygame.transform.scale(start, (400, 400))

click_start = pygame.image.load('image/click_start.png').convert_alpha()
click_start = pygame.transform.scale(click_start, (410, 410))

game_over = pygame.image.load("image/game_over.png").convert_alpha()
game_over_rect = game_over.get_rect(center=(400, 300))

paused = pygame.image.load("image/paused.png").convert_alpha()
paused_rect = paused.get_rect(center=(400, 200))

restart = game_font.render('Press space to restart', False, (0, 0, 0))
restart_rec = restart.get_rect(center=(400, 500))

quit_menu = game_font.render('Press ESC to quit', False, (0, 0, 0))
quit_menu_rec = quit_menu.get_rect(center=(400, 550))

score_bg = pygame.image.load("image/score_bg.png").convert_alpha()
score_bg = pygame.transform.scale(score_bg, (800, 600))


replay = pygame.image.load("image/replay.png").convert_alpha()

menu_bg = pygame.image.load("image/menu_bg.png").convert_alpha()
menu_bg = pygame.transform.scale(menu_bg, (800, 600))

tutorial = pygame.image.load("image/tutorial.png").convert_alpha()


# Game states for checking what to display
start_game = False
menu_screen = False
play_game = False
end_screen = False
over_screen = False
paused_screen = False
tutorial_screen = False
highscore_screen = False
music_load = False
restart_state = False
arrow_press = False

# Setting the song speed and the status of the song
play_music = False
song_timer = 0
song_speed = 4
c_hit = 0


# Arrow coordinates
rarrowY = []
larrowY = []
uarrowY = []
darrowY = []

rarrowX = []
larrowX = []
uarrowX = []
darrowX = []

# Key states

rarrow_key = "idle"
larrow_key = "idle"
darrow_key = "idle"
uarrow_key = "idle"

# Score
score_value = 0


# Player health
p_health = 1000

# Class that reads a file of times to give the y coordinates the arrow should be spawned at


class Note_timing:
    def __init__(self, file, song):
        self.file = file
        self.song = song

    def get_y(self):
        global song_score
        self.timing = open(self.file, "r")
        self.timing = self.timing.read()
        self.timing = self.timing.split(",")
        song_score = len(self.timing)
        for i in range(len(self.timing)):
            self.timing[i] = float(self.timing[i])
            self.song.append(-(song_speed * 60) * (self.timing[i]) + 515)
            choice([rarrowY, larrowY, uarrowY, darrowY]).append(self.song[i])


# Music Note Timings
unravel_note_timing = []
unravel = Note_timing("timing/unravel_timing.txt", unravel_note_timing)

rickroll_note_timing = []
rickroll = Note_timing("timing/rickroll_timing.txt", rickroll_note_timing)

harumachiclover_note_timing = []
harumachiclover = Note_timing("timing/harumachiclover_timing.txt", harumachiclover_note_timing)

furelise_note_timing = []
furelise = Note_timing("timing/furelise_timing.txt", furelise_note_timing)

mario_note_timing = []
mario = Note_timing("timing/mario_timing.txt", mario_note_timing)


# Music length in seconds
unravel_length = 92
rickroll_length = 38
harumachiclover_length = 37
furelise_length = 46
mario_length = 84


# Class that will show the grade of the user by detecting score


def get_grade(score_value, song_score):
    if score_value / song_score >= 0.9:
        a_grade = pygame.image.load("image/a_grade.png").convert_alpha()
        a_grade = pygame.transform.scale(a_grade, (300, 300))
        a_rect = a_grade.get_rect(center=(200, 300))
        screen.blit(a_grade, a_rect)
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value) + " / " + str(song_score), False, (255, 255, 255))
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 225))

    elif score_value / song_score >= 0.75 and score_value / song_score < 0.9:
        b_grade = pygame.image.load("image/b_grade.png").convert_alpha()
        b_grade = pygame.transform.scale(b_grade, (300, 300))
        b_rect = b_grade.get_rect(center=(200, 300))
        screen.blit(b_grade, b_rect)
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value) + " / " + str(song_score), False, (255, 255, 255))
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 225))

    elif score_value / song_score >= 0.6 and score_value / song_score < 0.75:
        c_grade = pygame.image.load("image/c_grade.png").convert_alpha()
        c_grade = pygame.transform.scale(c_grade, (300, 300))
        c_rect = c_grade.get_rect(center=(200, 300))
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value) + " / " + str(song_score), False, (255, 255, 255))
        screen.blit(c_grade, c_rect)
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 260))

    else:
        d_grade = pygame.image.load("image/d_grade.png").convert_alpha()
        d_grade = pygame.transform.scale(d_grade, (300, 300))
        d_rect = d_grade.get_rect(center=(200, 300))
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value) + " / " + str(song_score), False, (255, 255, 255))
        screen.blit(d_grade, d_rect)
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 225))


# Draws the health bar for the player

def display_highscore():
    unravel_high = end_font.render("Unravel : " + str(highscore_list[0]), False, (64, 64, 64))
    rickroll_high = end_font.render("Rick Roll : " + str(highscore_list[1]), False, (64, 64, 64))
    harumachiclover_high = end_font.render("Harumachi Clover : " + str(highscore_list[2]), False, (64, 64, 64))
    furelise_high = end_font.render("Fur Elise : " + str(highscore_list[3]), False, (64, 64, 64))
    mario_high = end_font.render("Mario theme : " + str(highscore_list[4]), False, (64, 64, 64))

    screen.blit(unravel_high, (200, 30))
    screen.blit(rickroll_high, (200, 130))
    screen.blit(harumachiclover_high, (200, 230))
    screen.blit(furelise_high, (200, 330))
    screen.blit(mario_high, (200, 430))


class Healthbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_health = 800
        self.target_health = 1000
        self.max_health = 1000
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5

        self.image = pygame.Surface((self.health_bar_length, 25))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(10, 10))
    # When the player takes damage

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    # When health needs to be added to the healthbar

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health
    # Allows me to set the health to a certain amount

    def set_health(self, amount):
        self.target_health = amount

    def update(self):
        self.health()

    def health(self):

        transition_length = 0
        transition_color = (0, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_length = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 255, 0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_length = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_length = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(10, 10, health_bar_length, 25)
        transition_bar = pygame.Rect(health_bar.right, 10, transition_length, 25)

        pygame.draw.rect(screen, (255, 0, 0), health_bar)

        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.health_bar_length, 25), 4)

        transition_bar.normalize()
        pygame.draw.rect(screen, transition_color, transition_bar)


healthbar = pygame.sprite.GroupSingle(Healthbar())

# Class that displays buttons and checks mouse colllision


class Img_Button:

    def __init__(self, x, y, image, image2, ):
        self.image = image
        self.image2 = image2
        self.x = x
        self.y = y
        self.clicked = False

    def draw_button(self):
        action = False

        mouse_pos = pygame.mouse.get_pos()
        button_rect = self.image.get_rect(center=(self.x, self.y))
        button_rect_2 = self.image2.get_rect(center=(self.x, self.y))

        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                screen.blit(self.image, button_rect_2)

            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                action = True

            else:
                screen.blit(self.image2, button_rect)
        else:
            screen.blit(self.image, button_rect)
        return action


# Class that draws rectangles and text as buttons,  also checks mouse colllision

class Word_Button():

    # colours for button and text
    button_col = (255, 192, 203)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (255, 255, 255)
    height = 70

    def __init__(self, x, y, text, width):
        self.x = x
        self.y = y
        self.text = text
        self.clicked = False
        self.width = width

    def draw_button(self):

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add text to button
        text_img = game_font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))

        return action

# A sprite class that will spawin in the arrows


class Arrow(pygame.sprite.Sprite):
    def __init__(self, type, x, y, x_change, y_change):

        super().__init__()
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change

        if type == "rarrow":
            rarrow = pygame.image.load('image/r_arrow.png').convert_alpha()
            rarrow = pygame.transform.scale(rarrow, (50, 50))
            self.frames = [rarrow]

        elif type == "larrow":
            larrow = pygame.image.load('image/l_arrow.png').convert_alpha()
            larrow = pygame.transform.scale(larrow, (50, 50))
            self.frames = [larrow]

        elif type == "uarrow":
            uarrow = pygame.image.load('image/u_arrow.png').convert_alpha()
            uarrow = pygame.transform.scale(uarrow, (50, 50))
            self.frames = [uarrow]

        else:
            darrow = pygame.image.load('image/d_arrow.png').convert_alpha()
            darrow = pygame.transform.scale(darrow, (50, 50))
            self.frames = [darrow]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # This is for the animation of the arrow which I haven't gotten around to do (please ignore)
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    # Update the arrow

    def update(self):
        global c_hit

        if c_hit == 0 and arrow_press:
            self.hit()
            c_hit += 1

        elif not arrow_press:
            self.animation_state()
            self.rect.x += self.x_change
            self.rect.y += self.y_change
            self.destroy()

    # Deletes the arrow when it is out of screen

    def destroy(self):
            global p_health
            if self.rect.y >= 632:
                healthbar.sprite.get_damage(100)
                p_health -= 100
                self.kill()

    def pause(self):
        self.y_change = 0

    def unpause(self):
        self.y_change = song_speed

    # Definition that detects whether an arrow has been "hit" and will delete the arrow and add score
    def hit(self):
        global score_value
        global p_health

        if rarrow_key == "pressed":
            if (self.rect.y <= 535 and self.rect.y >= 450):
                self.kill()
                healthbar.sprite.get_health(20)
                p_health += 20
                score_value += 1
            elif self.rect.y < 440 and self.rect.y >= 375:
                healthbar.sprite.get_damage(50)
                p_health -= 50
                self.kill()

        if larrow_key == "pressed":
            if (self.rect.y <= 535 and self.rect.y >= 450):
                self.kill()
                healthbar.sprite.get_health(20)
                p_health += 20
                score_value += 1
            elif self.rect.y < 440 and self.rect.y >= 375:
                healthbar.sprite.get_damage(50)
                p_health -= 50
                self.kill()

        if uarrow_key == "pressed":
            if (self.rect.y <= 535 and self.rect.y >= 440):
                self.kill()
                healthbar.sprite.get_health(20)
                p_health += 20
                score_value += 1
            elif self.rect.y < 410 and self.rect.y >= 355:
                healthbar.sprite.get_damage(50)
                p_health -= 50
                self.kill()

        if darrow_key == "pressed":
            if (self.rect.y <= 535 and self.rect.y >= 440):
                self.kill()
                healthbar.sprite.get_health(20)
                p_health += 20
                score_value += 1
            elif self.rect.y < 410 and self.rect.y >= 355:
                healthbar.sprite.get_damage(50)
                p_health -= 50
                self.kill()


# Groups
rarrow_group = pygame.sprite.Group()
larrow_group = pygame.sprite.Group()
uarrow_group = pygame.sprite.Group()
darrow_group = pygame.sprite.Group()

# Adding each arrow to their specified group for spawning


def arrow_spawn():

    for i in range(len(rarrowY)):
        rarrow_group.add(Arrow("rarrow", (550), rarrowY[i], 0, song_speed))
    for i in range(len(darrowY)):
        darrow_group.add(Arrow("darrow", (450), darrowY[i], 0, song_speed))
    for i in range(len(larrowY)):
        larrow_group.add(Arrow("larrow", (250), larrowY[i], 0, song_speed))
    for i in range(len(uarrowY)):
        uarrow_group.add(Arrow("uarrow", (350), uarrowY[i], 0, song_speed))


# Button
start_button = Img_Button(400, 300, start, click_start)
replay_button = Word_Button(450, 350, "Replay", 200)

unravel_button = Word_Button(300, 10, "Unravel", 200)
rickroll_button = Word_Button(300, 110, "Rick roll", 200)
harumachiclover_button = Word_Button(250, 210, "Harumachi Clover", 300)
furelise_button = Word_Button(300, 310, "Fur Elise", 200)
mario_button = Word_Button(300, 410, "Mario", 200)


resume_button = Word_Button(165, 450, "Resume", 200)
quit_button = Word_Button(465, 450, "Quit", 200)

quit_button2 = Word_Button(450, 450, "Quit", 200)


tutorial_button = Word_Button(10, 525, "Tutorial", 200)
highscore_button = Word_Button(590, 525, "Highscores", 200)

back_button = Word_Button(10, 10, "Back", 200)
back_button2 = Word_Button(10, 525, "Back", 200)

# Timer
arrow_timer = pygame.USEREVENT + 1
pygame.time.set_timer(arrow_timer, 1000)


# A class that shows the score on the screen
def display_score(x, y):
    score = game_font.render("Score : " + str(score_value), False, (64, 64, 64))
    screen.blit(score, (x, y))


running = True
# Main loop
while running:

    clock.tick(60)

    # Detects user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == arrow_timer and play_game:
            song_timer += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rarrow_key = "pressed"
            if event.key == pygame.K_LEFT:
                larrow_key = "pressed"
            if event.key == pygame.K_DOWN:
                darrow_key = "pressed"
            if event.key == pygame.K_UP:
                uarrow_key = "pressed"
            # Detects the space bar when in game over screen to restart
            if event.key == pygame.K_SPACE and not play_game and start_game and not menu_screen and not paused_screen:
                play_game = True
                restart_state = True
                arrow_spawn()
                p_health = 1000
                score_value = 0
                song_timer = 0
                healthbar.sprite.set_health(1000)

            if event.key == pygame.K_ESCAPE and play_game and start_game:
                for i in (rarrow_group):
                    i.pause()
                for i in (darrow_group):
                    i.pause()
                for i in (larrow_group):
                    i.pause()
                for i in (uarrow_group):
                    i.pause()

                paused_screen = True
                play_game = False
                menu_screen = False

            if event.key == pygame.K_ESCAPE and not play_game and over_screen:
                rarrow_group.empty()
                larrow_group.empty()
                uarrow_group.empty()
                darrow_group.empty()
                menu_screen = True
                over_screen = False

    # The game has just started and will show the starting menu/Logo
    if not start_game and not play_game and not end_screen and not paused_screen:
        screen.blit(start_bg, (0, 0))
        if start_button.draw_button():

            start_game = True
            menu_screen = True

    # Shows menu
    elif start_game and menu_screen:

        screen.blit(menu_bg, (0, 0))

        # Ints the highscores from the file

        highscore = open("highscorefile.txt", "r")
        highscore_list = highscore.read()
        highscore_list = (highscore_list.split(","))

        for i in range(len(highscore_list)):
            highscore_list[i] = int(highscore_list[i])

        # reset all the arrow timings
        song_timer = 0

        rarrowY = []
        larrowY = []
        uarrowY = []
        darrowY = []

        rarrowX = []
        larrowX = []
        uarrowX = []
        darrowX = []

        if music_load:
            pygame.mixer.music.unload()
            music_load = False

        # All the buttons on the menu
        if unravel_button.draw_button():
            if not music_load:
                pygame.mixer.music.load("music/unravel.mp3")
                pygame.mixer.music.set_volume(0.05)
                unravel.get_y()
                arrow_spawn()
                song_length = unravel_length
                music_load = True
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)
            play_game = True
            menu_screen = False
            song_played = "unravel"

        if rickroll_button.draw_button():
            if not music_load:
                pygame.mixer.music.load("music/rickroll.mp3")
                pygame.mixer.music.set_volume(0.05)
                rickroll.get_y()
                arrow_spawn()
                song_length = rickroll_length
                music_load = True
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)
            play_game = True
            menu_screen = False

            song_played = "rickroll"

        if harumachiclover_button.draw_button():
            if not music_load:
                pygame.mixer.music.load("music/harumachiclover.mp3")
                pygame.mixer.music.set_volume(0.05)
                harumachiclover.get_y()
                arrow_spawn()
                song_length = harumachiclover_length
                music_load = True
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)
            play_game = True
            menu_screen = False

            song_played = "harumachiclover"

        if furelise_button.draw_button():
            if not music_load:
                pygame.mixer.music.load("music/furelise.mp3")
                pygame.mixer.music.set_volume(0.05)
                furelise.get_y()
                arrow_spawn()
                song_length = furelise_length
                music_load = True
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)
            play_game = True
            menu_screen = False

            song_played = "furelise"

        if mario_button.draw_button():
            if not music_load:
                pygame.mixer.music.load("music/mario.mp3")
                pygame.mixer.music.set_volume(0.05)
                mario.get_y()
                arrow_spawn()
                song_length = mario_length
                music_load = True
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)
            play_game = True
            menu_screen = False

            song_played = "mario"

        if tutorial_button.draw_button():
            tutorial_screen = True
            menu_screen = False

        if highscore_button.draw_button():
            highscore_screen = True
            menu_screen = False

    elif tutorial_screen and not menu_screen:
        screen.blit(tutorial, (0, 0))

        if back_button.draw_button():
            tutorial_screen = False
            menu_screen = True

    elif highscore_screen and not menu_screen:
        screen.blit(menu_bg, (0, 0))
        display_highscore()

        if back_button2.draw_button():
            highscore_screen = False
            menu_screen = True

    # A song has been selected has been pressed and the game will start
    elif start_game and play_game and not end_screen:

        # Checks if the game has been restarted
        if restart_state:
            pygame.mixer.music.rewind()
            restart_state = False

        # Checks whether music should be played or not
        if not play_music:
            pygame.mixer.music.play()
            play_music = True

        screen.blit(start_bg, (0, 0))
        screen.blit(background, (0, 0))
        healthbar.draw(screen)
        healthbar.update()

        # Detects when the player "hits an arrow"
        if rarrow_key == "pressed":
            arrow_press = True
            rarrow_group.update()
            rarrow_key = "idle"
            c_hit = 0
            arrow_press = False

        elif larrow_key == "pressed":
            arrow_press = True
            larrow_group.update()
            larrow_key = "idle"
            c_hit = 0
            arrow_press = False

        elif uarrow_key == "pressed":
            arrow_press = True
            uarrow_group.update()
            arrow_press = True
            uarrow_key = "idle"
            c_hit = 0
            arrow_press = False

        elif darrow_key == "pressed":
            arrow_press = True
            darrow_group.update()
            darrow_key = "idle"
            c_hit = 0
            arrow_press = False

        # Sets the game state to false when health drops to 0
        if p_health <= 0:
            play_game = False
            over_screen = True

        # Sets the game state to false when game ends, but set end_screen to true to display score
        if song_timer == (song_length - 1):
            play_music = False
            pygame.mixer.music.pause()
            play_game = False
            end_screen = True

        # Drawing and updating the arrows
        rarrow_group.draw(screen)
        larrow_group.draw(screen)
        darrow_group.draw(screen)
        uarrow_group.draw(screen)

        rarrow_group.update()
        larrow_group.update()
        darrow_group.update()
        uarrow_group.update()

        # Showing the scoree
        display_score(625, 10)

    # Pause screen

    elif start_game and not play_game and paused_screen and not menu_screen:
        screen.blit(start_bg, (0, 0))
        screen.blit(paused, paused_rect)
        pygame.mixer.music.pause()

        if resume_button.draw_button():
            for i in (rarrow_group):
                i.unpause()
            for i in (darrow_group):
                i.unpause()
            for i in (larrow_group):
                i.unpause()
            for i in (uarrow_group):
                i.unpause()
            play_game = True
            paused_screen = False
            pygame.mixer.music.unpause()

        if quit_button.draw_button():
            rarrow_group.empty()
            larrow_group.empty()
            uarrow_group.empty()
            darrow_group.empty()

            paused_screen = False
            menu_screen = True
            play_music = False

    # Shows the game over screen and allows for restart
    elif not play_game and not end_screen and not menu_screen and over_screen:
        screen.blit(start_bg, (0, 0))
        screen.blit(game_over, game_over_rect)
        screen.blit(restart, restart_rec)
        screen.blit(quit_menu, quit_menu_rec)
        play_music = False
        pygame.mixer.music.pause()
        rarrow_group.empty()
        larrow_group.empty()
        uarrow_group.empty()
        darrow_group.empty()

    # Shows end screen and the score
    elif start_game and not play_game and end_screen:
        screen.blit(score_bg, (0, 0))
        get_grade(score_value, song_score)

        # Updates the highscores depending on what song it is

        if song_played == "unravel":
            if score_value > highscore_list[0]:

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                highscore_w = open("highscorefile.txt", "r+")
                highscore_w.seek(0)
                score_str = str(score_value)
                highscore_w.write(score_str)

        elif song_played == "rickroll":
            if score_value > highscore_list[1]:

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                highscore_w = open("highscorefile.txt", "r+")
                highscore_w.seek(5)
                score_str = str(score_value)
                highscore_w.write(score_str)

        elif song_played == "harumachiclover":
            if score_value > highscore_list[2]:

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                highscore_w = open("highscorefile.txt", "r+")
                highscore_w.seek(9)
                score_str = str(score_value)
                highscore_w.write(score_str)

        elif song_played == "furelise":
            if score_value > highscore_list[3]:

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                highscore_w = open("highscorefile.txt", "r+")
                highscore_w.seek(13)
                score_str = str(score_value)
                highscore_w.write(score_str)

        elif song_played == "mario":
            if score_value > highscore_list[4]:

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                new_high = end_font.render(" New High Score !", False, (255, 255, 255))
                screen.blit(new_high, (400, 75))

                highscore_w = open("highscorefile.txt", "r+")
                highscore_w.seek(17)
                score_str = str(score_value)
                highscore_w.write(score_str)

        # Replay button

        if replay_button.draw_button():
            song_timer = 0
            play_game = True
            end_screen = False
            restart_state = True
            arrow_spawn()
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)

        # Quit to menu button

        if quit_button2.draw_button():
            rarrow_group.empty()
            larrow_group.empty()
            uarrow_group.empty()
            darrow_group.empty()

            end_screen = False
            menu_screen = True
            play_music = False

    pygame.display.update()

pygame.quit()
