import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Başlık")

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # X yani kapatma tuşuna bastığımız durum
            gameExit = True #döngüyü sonlandırır ve ekran kapanır


pygame.quit()
quit()
