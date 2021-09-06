import pygame
import random
import math
import time
from pygame import mixer
from random import randint, choice
#pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
#pygame.init()
#clock = pygame.time.Clock()
#screen = pygame.display.set_mode((800, 600))

song_timer = 0
song_speed = 4

f = open("arrow_placement", "w")
rarrowY= []
larrowY = []
uarrowY = []
darrowY= []

rarrowX = []
larrowX = []
uarrowX = []
darrowX= []

##mixer.music.load("music.mp3")
##mixer.music.set_volume(0.09)
##mixer.music.play()


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
            self.song.append(-(song_speed*60)*(self.timing[i])+475)
            #choice([rarrowY, larrowY, uarrowY, darrowY]).append(self.song[i])

#Music Note Timings
unravel_note_timing = []
unravel = Note_timing("unravel_timing.txt", unravel_note_timing)
unravel.get_y()

#print(rarrowY,"\n", larrowY,"\n", uarrowY,"\n", darrowY)
print(unravel_note_timing)
#Music length:
unravel_length = 240

start_time = time.time()


for i in range(len(unravel_note_timing)):
    f.write(str(unravel_note_timing[i])+ ", ")
f.close()
    
#running = True
#while running:
    #clock.tick(60)
    #elapsed_time = time.time() - start_time
    ##print(elapsed_time)
            
    #seconds = pygame.time.get_ticks()/1000


    ## RGB = Red, Green, Blue
    #screen.fill((255, 255, 255))
    ## Background Image

    
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
            
    ## the time at which things happen.
    #when_things_happen = unravel_note_timing
    #happening = [x for x in when_things_happen if  x <= elapsed_time]
    ## now since things have happened, we remove them from the list.
    #for x in happening:
        #print(elapsed_time)  
        #when_things_happen.remove(x)

    
    #pygame.display.update() 
