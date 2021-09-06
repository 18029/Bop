import pygame
import random
import math
import time
from pygame import mixer

pygame.init()
mixer.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png').convert_alpha()
background = pygame.transform.scale(background , (800, 600))
start_bg = pygame.image.load('start_bg.png').convert_alpha()
start_bg = pygame.transform.scale(start_bg , (800, 600))
start = pygame.image.load('start.png').convert_alpha()
start = pygame.transform.scale(start , (400, 400))
click_start = pygame.image.load('click_start.png').convert_alpha()
click_start = pygame.transform.scale(click_start , (410, 410))

start_game = False


class Button:
 
    def __init__(self, x, y, image, image2):
        self.image = image
        self.image2 = image2
        self.x = x
        self.y = y
        self.clicked = False
        
        

    def draw_button(self):

        action = False

        mouse_pos = pygame.mouse.get_pos()
        button_rect =  self.image.get_rect(center = (self.x, self.y))
        button_rect_2 = self.image2.get_rect(center = (self.x, self.y))
     

       
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
                screen.blit(self.image2, button_rect_2)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == False:
                self.clicked = True
                action = True
                screen.blit(self.image,button_rect)
            else:
                screen.blit(self.image,button_rect)
        else:
            screen.blit(self.image,button_rect)
        return action




class Arrow(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == "rarrow":
    
            rarrow = pygame.image.load('r_arrow.png').convert_alpha()
            rarrow = pygame.transform.scale(rarrow, (32, 32))
            self.frames = [rarrow]
              
        else:
            pass
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
        
        def animation_state(self):
            self.animation_index += 0.1
            if self.animation >= (self.frames): self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
            
        def update(self):
            self.animation_state()
        
clock = pygame.time.Clock()      


#Groups
arrow_group = pygame.sprite.Group()
arrow_group.add(Arrow("rarrow"))


start_button = Button(400, 300, start, click_start)

running = True
while running:
   
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                
                   
            running = False
            
            
    if start_game == False:
        
        screen.blit(start_bg, (0, 0))
        start_button.draw_button()
        
        if start_button.draw_button():
            pass
            
            #screen.blit(start_bg, (0,0))
            #screen.blit(background,(0, 0))
         
            
    

    

    
    pygame.display.update()