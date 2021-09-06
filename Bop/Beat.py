import pygame
import random
import math
import time
from pygame import mixer

note_time = []
space_key = "idle"


f = open("unravel_timing.txt", "w")

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

x = 32 
y = 32
            
            
game_over = pygame.image.load("game_over.png").convert_alpha()   
 
uarrow = pygame.image.load('u_arrow.png').convert_alpha()
uarrow = pygame.transform.scale(uarrow, (x, y))   

mixer.music.load("music.mp3")
mixer.music.set_volume(0.09)
mixer.music.play()

running = True
while running:
    clock.tick(120)
    
            
    seconds = pygame.time.get_ticks()/1000


    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))
    # Background Image
    
    screen.blit(uarrow, (50, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for i in range(len(note_time)):    
                f.write(str(note_time[i]) + ", ")
            f.close()
            running = False
    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_key = "pressed"  
                note_time.append(seconds)     
                
   
    screen.blit(game_over, (300, 150))
    
    
    pygame.display.update() 



#g = open("unravel_timing.txt", "r")
#h = g.read()

#h = (h.split(","))



#print(h)

#y= []
#class Note_timing:
    #def __init__(self, file, song):
        #self.file = file
        #self.song = song

    #def get_y(self):
     
        #self.timing =  open(self.file, "r")
        #self.timing = self.timing.read()
        #self.timing = self.timing.split(",")
        
        #for i in range(len(self.timing)):
            #self.timing[i] = float(self.timing[i])
            #self.song.append(-self.timing[i]*(song_speed*60)+516)
     
     
   
   
    
            
              

     
    
        
        
        
#a = 
#a.file_read()