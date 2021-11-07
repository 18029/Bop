import pygame
import random
import math
import time
from pygame import mixer
global counter
pygame.init()
mixer.init()

timer = 0
 

timing = [2.367, 2.611, 2.989, 3.423, 3.639, 4.101, 4.551, 5.023, 5.424, 5.848, 6.079, 6.774, 7.122, 7.559, 7.811]



list_length = len(timing)

start_ticks=pygame.time.get_ticks() #starter tick
r_arrow = pygame.image.load('r_arrow.png')
r_arrow = pygame.transform.scale(r_arrow, (32, 32))

screen = pygame.display.set_mode((800, 600))
unravel_bg = pygame.image.load('unravel_bg.png')
unravel_bg = pygame.transform.scale(unravel_bg , (800, 600))
background = pygame.image.load('background.png')
background = pygame.transform.scale(background , (800, 600))
mixer.music.load("music.mp3")
mixer.music.set_volume(0.09)
mixer.music.play()


clock = pygame.time.Clock()


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


rarrow = []
rarrowX = []
rarrowY = []
rarrowX_change = []
rarrowY_change = []
rarrowW = []
rarrowH = []

hi = 0


def isCollision(arrowX, arrowY, arrow1X, arrow1Y):
 distance = math.sqrt(math.pow(arrowX - arrow1X, 2) + (math.pow(arrowY - arrow1Y, 2)))
 if distance < 50:
  return True
 else:
  pass


rarrow_key = "idle"


for i in range(len(timing)):

 rarrow.append((r_arrow))
 rarrowY.append(-(timing[i]-0.3)*(180)+516)
 rarrowX.append((1860 + rarrowY[i]) / 4)
 rarrowX_change.append(0.75)
 rarrowY_change.append(3)
 rarrowW.append(32)
 rarrowH.append(32)
 


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def rarrowxy(x, y, i):
    screen.blit(rarrow[i], (x, y))



running = True
while running:
 
    clock.tick(60)
   

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))
    # Background Image
    #screen.blit(unravel_bg, (0,0))
    screen.blit(background, (0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rarrow_key = "pressed"

 
    for i in range(list_length):
     rarrowxy(rarrowX[i], rarrowY[i], i)
     #print(len(rarrowX), len(rarrowY))
     #print(list_length - hi)
   
  
  
        

     rarrowY[i] += rarrowY_change[i]
     rarrowX[i] += rarrowX_change[i]
     #rarrow[i] = pygame.transform.smoothscale(rarrow[i], (rarrowW[i], rarrowH[i]))
     #rarrowW[i] += 1
     #rarrowH[i] += 1

     if rarrow_key == "pressed" and rarrowY[i] <= 536 and rarrowY[i] >= 464:
      
      score_value += 1
      rarrowX.remove(rarrowX[i])
      rarrowY.remove(rarrowY[i])     
      rarrow_key = "idle"      
      list_length -= 1
      #rarrowX[i] = 2000
      #rarrowY[i] = -2000
      break
      
      
     elif rarrow_key == "pressed" and (rarrowY[i] >= 536 or rarrowY[i] <= 464):
      rarrow_key = "idle"
      print("miss")
      
      
      
     #elif rarrowY[i] >= 600
    show_score(10, 10)
     

  
  

   

    pygame.display.update()