import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Başlık")

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event) # siyah ekrandaki mouse pozisyonunu yazar


pygame.quit()
quit()