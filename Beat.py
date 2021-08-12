import pygame
import random
import math
import time
from pygame import mixer

note_time = []
space_key = "idle"


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))


mixer.music.load("music.mp3")
mixer.music.set_volume(0.09)
mixer.music.play()

running = True
while running:
    clock.tick(60)
    
            
    seconds = pygame.time.get_ticks()/1000    

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))
    # Background Image


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                
            print(note_time)            
            running = False
    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_key = "pressed"  
                note_time.append(seconds)     
                
                
                
    
    
    pygame.display.update()


