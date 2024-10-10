import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Triangle")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a triangle
    pygame.draw.polygon(screen, (255, 0, 0), [(500, 100), (300, 200), (500, 200)])

    # Update the display
    pygame.display.flip()

pygame.quit()
