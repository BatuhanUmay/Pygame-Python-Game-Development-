import pygame 

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

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tanks")

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

clock = pygame.time.Clock()
block_size = 20


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
        

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() #(sol kılik,,sağ kılik)
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
                
            if action == "controls":
                pass
                
            if action == "play":
                gameLoop()
                
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text, black, x, y, width, height)


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

        button("play", 150,500,100,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)
    

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