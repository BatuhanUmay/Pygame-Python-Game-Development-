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


def square(startPoint, fullSize):
    node_1 = [startPoint[0], startPoint[1]]
    node_2 = [startPoint[0] + fullSize, startPoint[1]]
    node_3 = [startPoint[0], startPoint[1] + fullSize]
    node_4 = [startPoint[0] + fullSize, startPoint[1] + fullSize]
    
    #top line
    pygame.draw.line(gameDisplay, white, (node_1), (node_2))
    #bottom line
    pygame.draw.line(gameDisplay, white, (node_3), (node_4))
    #left line
    pygame.draw.line(gameDisplay, white, (node_1), (node_3))
    #right line
    pygame.draw.line(gameDisplay, white, (node_2), (node_4))
    
    pygame.draw.circle(gameDisplay, light_green, node_1, 5)
    pygame.draw.circle(gameDisplay, light_green, node_2, 5)
    pygame.draw.circle(gameDisplay, light_green, node_3, 5)
    pygame.draw.circle(gameDisplay, light_green, node_4, 5)
    
def gameLoop():    
    
    location = [300,200]
    size = 200
    
    current_move = 0
    
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()             
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_move = -5        
                if event.key == pygame.K_RIGHT:
                    current_move = 5        
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    current_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    current_move = 0
                            
        gameDisplay.fill(black)   
        
        location[0] += current_move
        
        square(location, size)
        pygame.display.update()
                   
        clock.tick(FPS)       
    

gameLoop() 
