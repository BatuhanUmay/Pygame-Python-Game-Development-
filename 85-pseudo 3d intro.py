import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)

red =(200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

display_width = 800
display_height = 600

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("3d")

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

FPS = 30
    
def gameLoop():    
    
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()             
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass        
                if event.key == pygame.K_RIGHT:
                    pass        
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pass
                            
        gameDisplay.fill(black)              
        clock.tick(FPS)       
    

gameLoop() 
