import pygame
import sys
import random
from pygame import mixer

pygame.init()
# Starting the mixer 
mixer.init() 

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)

# Load the background image
background_image = pygame.image.load("background1.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Loading the song 
mixer.music.load("pop sound.mp3")
# Setting the volume 
mixer.music.set_volume(50)


snake_size = 20
snake = [(width // 2, height // 2)]
food = (random.randint(0, width // snake_size - 1) * snake_size,
        random.randint(0, height // snake_size - 1) * snake_size)
direction = (0, -1)  # Initial direction: up

clock = pygame.time.Clock()

score = 0

def calculate_score():
    global score
    score += 1

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Score: " + str(score), True, (255, 255, 255))
    text_rect = text.get_rect(center=(width//2, height//2))
    window.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

while True:
    window.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #background img
    window.blit(background_image, (0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)


    elif keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)

    # Move the snake
    head = (snake[0][0] + direction[0] * snake_size,
            snake[0][1] + direction[1] * snake_size)
    snake.insert(0, head)
    
  # Check if the snake hits the boundaries or itself
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height or head in snake[1:]:
        game_over()
    

    
    # Check for collision with food
    if head == food:
        calculate_score()
        food = (random.randint(0, width // snake_size - 1) * snake_size,
                random.randint(0, height // snake_size - 1) * snake_size)
        # Start playing the song 
        mixer.music.play()
    else:
        snake.pop()

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(window, (255, 255, 255), (segment[0], segment[1], snake_size, snake_size))
    
    # Draw the food
    pygame.draw.rect(window, (255, 0, 0), (food[0], food[1], snake_size, snake_size))

    pygame.display.update()
    clock.tick(10) # Snake speed

pygame.quit()