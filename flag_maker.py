import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Flag")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (0, 50, 600, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, 150, 600, 100))
    pygame.draw.rect(screen, (0, 0, 255), (0, 250, 600, 100))

    pygame.draw.polygon(screen, (255, 255, 0), [
        (300, 150), (315, 185), (350, 185), (322, 210), 
        (335, 245), (300, 225), (265, 245), (278, 210), 
        (250, 185), (285, 185)
    ])

    pygame.display.flip()

pygame.quit()
