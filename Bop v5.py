import pygame
import random
import math
import time
from pygame import mixer
from random import randint, choice
clock = pygame.time.Clock()
pygame.mixer.pre_init(frequency = 22050, size = -16, channels = 2, buffer = 512)
pygame.init()


play_music = False

song_timer = 0
song_speed = 4


game_font = pygame.font.Font('Pixeltype.ttf', 50)
end_font = pygame.font.Font('Pixeltype.ttf', 80)
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background_1.png').convert_alpha()
background = pygame.transform.scale(background , (800, 600))
start_bg = pygame.image.load('start_bg.png').convert_alpha()
start_bg = pygame.transform.scale(start_bg , (800, 600))
start = pygame.image.load('start.png').convert_alpha()
start = pygame.transform.scale(start , (400, 400))
click_start = pygame.image.load('click_start.png').convert_alpha()
click_start = pygame.transform.scale(click_start , (410, 410))
game_over = pygame.image.load("game_over.png").convert_alpha()
game_over_rect = game_over.get_rect(center = (400, 300))
restart = game_font.render('Press space to restart',False,(0, 0, 0))
restart_rec = restart.get_rect(center = (400,500))
score_bg = pygame.image.load("score_bg1.png").convert_alpha()
score_bg = pygame.transform.scale(score_bg , (800, 600))
replay = pygame.image.load("replay.png").convert_alpha()


pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.05)            

pygame.mixer.music.play()
if play_music == False:
    pygame.mixer.music.pause()    


start_game = False
play_game = False
end_screen = False


rarrowY= []
larrowY = []
uarrowY = []
darrowY= []

rarrowX = []
larrowX = []
uarrowX = []
darrowX= []

#Key states

rarrow_key = "idle"
larrow_key = "idle"
darrow_key = "idle"
uarrow_key = "idle"

#Score
score_value = 0


#Player health
p_health = 1000


class Note_timing:
    def __init__(self, file, song):
        self.file = file
        self.song = song

    def get_y(self):
        global song_score
        self.timing =  open(self.file, "r")
        self.timing = self.timing.read()
        self.timing = self.timing.split(",")
        song_score = len(self.timing)
        for i in range(len(self.timing)):
            self.timing[i] = float(self.timing[i])
            self.song.append(-(song_speed*60)*(self.timing[i]-0.3)+500)
            choice([rarrowY, larrowY, uarrowY, darrowY]).append(self.song[i])
            
#Music Note Timings
unravel_note_timing = []
unravel = Note_timing("unravel_timing.txt", unravel_note_timing)
unravel.get_y()

#Music length:
unravel_length = 240


def get_grade(score_value, song_score):
    if score_value/song_score >= 0.9:
        a_grade = pygame.image.load("a_grade.png").convert_alpha()
        a_grade  = pygame.transform.scale(a_grade, (300, 300))
        a_rect = a_grade.get_rect(center = (200, 300))
        screen.blit(a_grade, a_rect)
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value)+" / " + str(song_score), False, (255, 255, 255))
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 225))
         
    elif score_value/song_score >= 0.75 and score_value/song_score < 0.9:
        b_grade = pygame.image.load("b_grade.png").convert_alpha()
        b_grade  = pygame.transform.scale(b_grade, (300, 300))
        b_rect = b_grade.get_rect(center = (200, 300))
        screen.blit(b_grade, b_rect)        
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value)+" / " + str(song_score), False, (255,255,255))
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 225))
        
    elif score_value/song_score >= 0.6 and score_value/song_score < 0.75:
        c_grade = pygame.image.load("c_grade.png").convert_alpha()
        c_grade  = pygame.transform.scale(c_grade, (300, 300))
        c_rect = c_grade.get_rect(center = (200, 300))
        total_score = end_font.render(" Total Score : ", False, (255,255,255))
        end_score = end_font.render(str(score_value)+" / " + str(song_score), False, (255,255,255))
        screen.blit(c_grade, c_rect) 
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 260))
 
    else:
        d_grade = pygame.image.load("d_grade.png").convert_alpha()
        d_grade  = pygame.transform.scale(d_grade, (300, 300))
        d_rect = d_grade.get_rect(center = (200, 300))
        total_score = end_font.render(" Total Score : ", False, (255, 255, 255))
        end_score = end_font.render(str(score_value)+" / " + str(song_score), False, (255, 255, 255))
        screen.blit(d_grade, d_rect) 
        screen.blit(total_score, (400, 175))
        screen.blit(end_score, (420, 225))


           
class Healthbar(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        
        self.current_health = 800
        self.target_health = 1000
        self.max_health = 1000
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5

        self.image = pygame.Surface((self.health_bar_length,25))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft = (10, 10))        

    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health
    
    def set_health(self, amount):
        self.target_health = amount

    def update(self):
        self.health()


    def health(self):
        transition_length = 0
        transition_color = (0,0,0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_length = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 255, 0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed 
            transition_length = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255,255,0)

        health_bar_length = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(10,10,health_bar_length,25)
        transition_bar = pygame.Rect(health_bar.right,10,transition_length,25)

        pygame.draw.rect(screen,(255,0,0),health_bar)

        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_length,25),4)	

        transition_bar.normalize()
        pygame.draw.rect(screen,transition_color,transition_bar)  


healthbar = pygame.sprite.GroupSingle(Healthbar())

class Button:
 
    def __init__(self, x, y, image, image2, ):
        self.image = image
        self.image2 = image2
        self.x = x
        self.y = y
        self.clicked = False
      
    def set_false(self):
        self.clicked = False

    def draw_button(self):

  

        mouse_pos = pygame.mouse.get_pos()
        button_rect =  self.image.get_rect(center = (self.x, self.y))
        button_rect_2 = self.image2.get_rect(center = (self.x, self.y))
     

       
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                
                screen.blit(self.image2, button_rect_2)
                
            else:
                screen.blit(self.image,button_rect)
        else:
            screen.blit(self.image,button_rect)
        return self.clicked




class Arrow(pygame.sprite.Sprite):
    def __init__(self,type, x, y, x_change, y_change):
           
        super().__init__()
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        
        if type == "rarrow":
    
            rarrow = pygame.image.load('r_arrow.png').convert_alpha()
            rarrow = pygame.transform.scale(rarrow, (50, 50))
            self.frames = [rarrow]
            
            
              
        elif type == "larrow":
            larrow = pygame.image.load('l_arrow.png').convert_alpha()
            larrow = pygame.transform.scale(larrow, (50, 50)) 
            self.frames = [larrow]  
            
    
                        
        elif  type == "uarrow":
            uarrow = pygame.image.load('u_arrow.png').convert_alpha()
            uarrow = pygame.transform.scale(uarrow, (50, 50))     
            self.frames = [uarrow] 
     
            
            
        else:
            darrow = pygame.image.load('d_arrow.png').convert_alpha()
            darrow = pygame.transform.scale(darrow, (50, 50))
            self.frames = [darrow] 

            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        
    def animation_state(self):
            self.animation_index += 0.1
            if self.animation_index >= len(self.frames): self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
             
    def update(self):
            self.animation_state()
            
            self.rect.x += self.x_change
            self.rect.y += self.y_change 
            self.hit()
            self.destroy()
            

    def destroy(self):
            global p_health
            if self.rect.y >= 632:
                healthbar.sprite.get_damage(200)
                p_health -= 200
                self.kill()
          
    
    def hit(self):
        global score_value   
        global p_health
        if rarrow_key == "pressed" and (self.rect.y <= 520 and self.rect.y >= 450):
            self.kill()
            healthbar.sprite.get_health(10)
            p_health += 10
            score_value += 1             
        if larrow_key == "pressed" and (self.rect.y <= 520 and self.rect.y >= 450):
            self.kill()
            healthbar.sprite.get_health(10)
            p_health += 10
            score_value += 1         
        if uarrow_key == "pressed" and (self.rect.y <= 520 and self.rect.y >= 450):
            self.kill()
            healthbar.sprite.get_health(10)
            p_health += 10
            score_value += 1           
        if darrow_key == "pressed" and (self.rect.y <= 520 and self.rect.y >= 450):
            self.kill()
            healthbar.sprite.get_health(10)
            p_health += 10
            score_value += 1 
      
#Groups
rarrow_group = pygame.sprite.Group()
larrow_group = pygame.sprite.Group()
uarrow_group = pygame.sprite.Group()
darrow_group = pygame.sprite.Group()


def arrow_spawn():   
        
    for i in range(len(rarrowY)):
        rarrow_group.add(Arrow("rarrow", (525), rarrowY[i], 0, 4))   
    for i in range(len(darrowY)):
        darrow_group.add(Arrow("darrow", (425), darrowY[i], 0, 4))
    for i in range(len(larrowY)):
        larrow_group.add(Arrow("larrow", (225), larrowY[i], 0, 4))   
    for i in range(len(uarrowY)):
        uarrow_group.add(Arrow("uarrow", (325), uarrowY[i], 0, 4))
    
arrow_spawn()     

#Button
start_button = Button(400, 300, start, click_start)
replay_button = Button(550 ,400, replay, replay)

#Timer
rarrow_timer = pygame.USEREVENT + 1
pygame.time.set_timer(rarrow_timer, 1000)



def display_score(x ,y):
    score = game_font.render("Score : " + str(score_value),False,(64,64,64))
    
    screen.blit(score, (x, y))

running = True
while running:
    
    clock.tick(60)
    

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == rarrow_timer and start_game == True:
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
            
            if event.key == pygame.K_SPACE and play_game == False and start_game == True:
                play_game = True
                pygame.mixer.music.rewind()
                arrow_spawn()    
                p_health = 1000
                score_value = 0
                healthbar.sprite.set_health(1000)
                
              
                
    if start_game == False and play_game == False and end_screen == False:
        
        screen.blit(start_bg, (0, 0))
        if start_button.draw_button():
            start_game = True
            play_game = True
    
    
    elif start_game == True and play_game == True and end_screen == False:
        play_music = True
        pygame.mixer.music.unpause()
        screen.blit(start_bg, (0,0))
        screen.blit(background,(0, 0))
        
        healthbar.draw(screen)
        healthbar.update()        
        
    
        
        if rarrow_key == "pressed":
            rarrow_group.update()
            rarrow_key = "idle"
        elif larrow_key == "pressed":
            larrow_group.update()
            larrow_key = "idle"
            
        elif uarrow_key == "pressed":
        
            uarrow_group.update()
            uarrow_key = "idle"                 
            
        elif darrow_key == "pressed":
            darrow_group.update()
            darrow_key = "idle"       
      
     
        if p_health <= 0:
            play_game = False
            
        if song_timer == (unravel_length - 1):
            play_music = False
            pygame.mixer.music.pause()
            play_game = False
            end_screen = True
            
        rarrow_group.draw(screen)
        larrow_group.draw(screen)
        darrow_group.draw(screen)
        uarrow_group.draw(screen)
        
        rarrow_group.update()
        larrow_group.update()
        darrow_group.update()
        uarrow_group.update()
         
        
        display_score(600, 10)                 
          
                 
    
    elif start_game == True and play_game == False and end_screen == False:
        screen.blit(start_bg, (0,0))
        screen.blit(game_over, game_over_rect)
        screen.blit(restart,restart_rec)
        play_music = False
        pygame.mixer.music.pause()
        rarrow_group.empty()
        larrow_group.empty()
        uarrow_group.empty()
        darrow_group.empty()        
   
    
    elif start_game == True and play_game == False and end_screen == True:
        screen.blit(score_bg, (0,0))
        get_grade(score_value, song_score)
        if replay_button.draw_button():
            play_music = True
            play_game = True
            end_screen = False
            pygame.mixer.music.rewind()
            p_health = 1000
            score_value = 0
            healthbar.sprite.set_health(1000)
            song_timer = 0
            replay_button.set_false()
            arrow_spawn()     
  
    pygame.display.update()