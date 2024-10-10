import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Shapes")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # Draw a circle
    pygame.draw.circle(screen, (0, 255, 0), (200, 200), 50)

    # Update the display
    pygame.display.flip()

pygame.quit()

import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Shapes")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    # Draw a circle
    pygame.draw.circle(screen, (0, 255, 0), (200, 200), 50)

    # Update the display
    pygame.display.flip()

pygame.quit()