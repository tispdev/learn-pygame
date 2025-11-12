import pygame
print("Pygame imported!")


#Initialize and Create Window

pygame.init()

screen = pygame.display.set_mode((600,200))
pygame.display.set_caption("My First Game!")


#Game Loop + Background Color
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100,150,200)) #RGB color
    pygame.draw.rect(screen, (255, 100, 100), (150, 100, 100, 50))
    pygame.display.flip()

pygame.quit()
