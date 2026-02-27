import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My Color Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 0))
    pygame.draw.circle(screen, (255, 255, 0), (250,200), 60)

    pygame.display.flip()

pygame.quit()
