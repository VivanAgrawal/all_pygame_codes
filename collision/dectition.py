import pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Collision Detection")

# Define two rectangles
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(200, 200, 50, 50)

# Set initial movement speed
speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    # Update rect1's position based on arrow key inputs
    if keys[pygame.K_LEFT]:
        rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        rect1.x += speed
    if keys[pygame.K_UP]:
        rect1.y -= speed
    if keys[pygame.K_DOWN]:
        rect1.y += speed

    # Check for collision
    if rect1.colliderect(rect2):
        print("Collision detected!")

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)

    pygame.display.flip()

pygame.quit()
