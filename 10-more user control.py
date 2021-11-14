import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Başlık")

lead_x = 300
lead_y = 300

lead_x_change = 0

gameExit = False

clock = pygame.time.Clock()

while not gameExit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            
        if event.type == pygame.KEYDOWN: #tuşa basmasan bile nokta oto olarak ilerler
            if event.key == pygame.K_LEFT:
                lead_x_change = -10

            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
                
        # if event.type == pygame.KEYUP: #tuşa basmazsan nokta ekranda ilerlemicek
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         lead_x_change = 0
         
    lead_x += lead_x_change
    
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
    pygame.display.update()
    
    clock.tick(15)

pygame.quit()
quit()