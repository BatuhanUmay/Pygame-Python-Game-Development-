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
    
    offset = int(fullSize / 2)
    node_5 =  [node_1[0] + offset, node_1[1] - offset]
    node_6 =  [node_2[0] + offset, node_2[1] - offset]
    node_7 =  [node_3[0] + offset, node_3[1] - offset]
    node_8 =  [node_4[0] + offset, node_4[1] - offset]   
    
    #top line
    pygame.draw.line(gameDisplay, white, (node_1), (node_2))
    #bottom line
    pygame.draw.line(gameDisplay, white, (node_3), (node_4))
    #left line
    pygame.draw.line(gameDisplay, white, (node_1), (node_3))
    #right line
    pygame.draw.line(gameDisplay, white, (node_2), (node_4))
 
    
    #top line
    pygame.draw.line(gameDisplay, white, (node_5), (node_6))
    #bottom line
    pygame.draw.line(gameDisplay, white, (node_7), (node_8))
    #left line
    pygame.draw.line(gameDisplay, white, (node_5), (node_7))
    #right line
    pygame.draw.line(gameDisplay, white, (node_6), (node_8))

    
    pygame.draw.circle(gameDisplay, light_green, node_1, 5)
    pygame.draw.circle(gameDisplay, light_green, node_2, 5)
    pygame.draw.circle(gameDisplay, light_green, node_3, 5)
    pygame.draw.circle(gameDisplay, light_green, node_4, 5)
    
    pygame.draw.circle(gameDisplay, light_green, node_5, 5)
    pygame.draw.circle(gameDisplay, light_green, node_6, 5)
    pygame.draw.circle(gameDisplay, light_green, node_7, 5)
    pygame.draw.circle(gameDisplay, light_green, node_8, 5)

    pygame.draw.line(gameDisplay, white, (node_1), (node_5))
    pygame.draw.line(gameDisplay, white, (node_2), (node_6))
    pygame.draw.line(gameDisplay, white, (node_3), (node_7))
    pygame.draw.line(gameDisplay, white, (node_4), (node_8))

    
def gameLoop():    
    
    location = [300,200]
    size = 200
    
    current_move = 0
    
    z_move = 0
    z_location = 1
    
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
                if event.key == pygame.K_UP:
                    z_move = -5  
                    current_move = -1      
                if event.key == pygame.K_DOWN:
                    z_move = 5        
                    current_move = 1      
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    current_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    z_move = 0
                    current_move = 0   

                            
        gameDisplay.fill(black)   
        
        if z_location > 200:
            z_move = 0
            
        z_location += z_move 
        
        current_size = int(size / (z_location * 0.1) )    
        
        location[0] += current_move
        
        square(location, current_size)
        pygame.display.update()
                   
        clock.tick(FPS)       
    

gameLoop() 