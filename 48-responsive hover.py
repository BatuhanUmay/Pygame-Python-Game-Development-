import pygame 

pygame.init()

white = (255,255,255)
black = (0,0,0)
red =(255,0,0)
green = (34,177,76)
yellow = (200,200,0)
light_green = (0,255,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tanks")

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

clock = pygame.time.Clock()
block_size = 20

def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)       

        message_to_screen("Welcome to Tanks!", green, -100, "large")
        message_to_screen("The objective is to shot and destroy!", black, -30,)
        message_to_screen("The enemy tank before they destroy you.", black, 10)
        message_to_screen("The more enemies you destroy, the harder they get.",
                          black, 50)
        
        cur = pygame.mouse.get_pos() #(x,y) şeklinde değer alır
        
        if 150+100 > cur[0] > 150 and 500+50 > cur[1] > 500:
            pygame.draw.rect(gameDisplay, light_green, (150,500,100,50))
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        pygame.draw.rect(gameDisplay, yellow, (350,500,100,50))
        pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        text_to_button("play", black, 150,500,100,50)
        text_to_button("controls", black, 350,500,100,50)
        text_to_button("quit", black, 550,500,100,50)

        pygame.display.update()
        clock.tick(15)
    

def text_object(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = ( (buttonx + (buttonwidth / 2)), (buttony + (buttonheight / 2)) )
    gameDisplay.blit(textSurf, textRect)
    

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = (int(display_width/2), int(display_height/2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def pause():
    paused = True
    
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", black, 25)
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
       

def gameLoop():
    global direction
    direction = "right"
    
    gameExit = False
    gameOver = False
    
    FPS = 15
    
    while not gameExit:
        if gameOver == True:
            message_to_screen("Game Over", red, -50, size = "large")
            message_to_screen("Press C to play again or Q to exit", black, 50, size = "large")
            pygame.display.update()
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()    
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()                   

        
        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    quit()
    
    
game_intro()
gameLoop() 