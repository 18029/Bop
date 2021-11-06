import pygame
import random
import math
import time
from pygame import mixer
from random import randint, choice
pygame.init()
mixer.init()
play_music = False
clock = pygame.time.Clock()    


song_speed = 4




screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png').convert_alpha()
background = pygame.transform.scale(background , (800, 600))
start_bg = pygame.image.load('start_bg.png').convert_alpha()
start_bg = pygame.transform.scale(start_bg , (800, 600))
start = pygame.image.load('start.png').convert_alpha()
start = pygame.transform.scale(start , (400, 400))
click_start = pygame.image.load('click_start.png').convert_alpha()
click_start = pygame.transform.scale(click_start , (410, 410))

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.05)            


pygame.mixer.music.play()

start_game = False


rarrowY= []
larrowY = []
uarrowY = []
darrowY= []

rarrowX = []
larrowX = []
uarrowX = []
darrowX= []



class Note_timing:
    def __init__(self, file, song):
        self.file = file
        self.song = song

    def get_y(self):
     
        self.timing =  open(self.file, "r")
        self.timing = self.timing.read()
        self.timing = self.timing.split(",")
        
        for i in range(len(self.timing)):
            self.timing[i] = float(self.timing[i])
            self.song.append(-self.timing[i]*(song_speed*60)+516)
            choice([rarrowY, larrowY, uarrowY, darrowY]).append(self.song[i])

#Music Note Timings
unravel_note_timing = []
unravel = Note_timing("unravel_timing.txt", unravel_note_timing)
unravel.get_y()


class Button:
 
    def __init__(self, x, y, image, image2, ):
        self.image = image
        self.image2 = image2
        self.x = x
        self.y = y
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
            rarrow = pygame.transform.scale(rarrow, (32, 32))
            self.frames = [rarrow]
            
            
              
        elif type == "larrow":
            larrow = pygame.image.load('l_arrow.png').convert_alpha()
            larrow = pygame.transform.scale(larrow, (32, 32)) 
            self.frames = [larrow]  
            
    
                        
        elif  type == "uarrow":
            uarrow = pygame.image.load('u_arrow.png').convert_alpha()
            uarrow = pygame.transform.scale(uarrow, (32, 32))     
            self.frames = [uarrow] 
     
            
            
        else:
            darrow = pygame.image.load('d_arrow.png').convert_alpha()
            darrow = pygame.transform.scale(darrow, (32, 32))
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
            self.destroy()

    def destroy(self):
            if self.rect.y >= 632: 
                self.kill()
#Groups
arrow_group = pygame.sprite.Group()


for i in range(len(rarrowY)):
    arrow_group.add(Arrow("rarrow", ((1860 + rarrowY[i]) / 4), rarrowY[i], 1, 4))
    
for i in range(len(darrowY)):
    arrow_group.add(Arrow("darrowY", ((1200- darrowY[i]) / 4), darrowY[i], -1, 4))
    

for i in range(len(larrowY)):
    arrow_group.add(Arrow("larrow", ((1200- larrowY[i]) / 4), larrowY[i], -1, 4))
    
for i in range(len(uarrowY)):
    arrow_group.add(Arrow("uarrowY", ((1200- uarrowY[i]) / 4), uarrowY[i], -1, 4))
    
        

#Button
start_button = Button(400, 300, start, click_start)


#Timer
rarrow_timer = pygame.USEREVENT + 1
pygame.time.set_timer(rarrow_timer, 1000)



running = True
while running:
    
    if play_music == False:
        pygame.mixer.music.pause() 
    clock.tick(60)

  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == rarrow_timer and start_game == True:
            pass
            
                      
            
            
    if start_game == False:
        
        screen.blit(start_bg, (0, 0))
        if start_button.draw_button():
            start_game = True
    
    elif start_game == True:
        play_music = True
        pygame.mixer.music.unpause()
        screen.blit(start_bg, (0,0))
        screen.blit(background,(0, 0))
        
        
        
        arrow_group.draw(screen)
        arrow_group.update()
      
    

    
    pygame.display.update()