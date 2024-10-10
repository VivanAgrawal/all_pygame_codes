import pygame
import random
import sys
from pygame import mixer

# Initialize Pygame
pygame.init()
# Starting the mixer 
mixer.init() 

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CAR_WIDTH, CAR_HEIGHT = 50, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
OBSTACLE_SPEED = 5

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CAR GAME!!")
font = pygame.font.Font(None, 36)

# Load the background image
background_image = pygame.image.load("bg.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Loading the song 
mixer.music.load("sound.mp3")
# Setting the volume 
mixer.music.set_volume(50)
# Start playing the song 
mixer.music.play()

# Load images
car_image = pygame.image.load("car2.jpg")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

score = 0

def calculate_score():
    global score
    score += 1

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Score: " + str(score), True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    window.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game variables
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 20
obstacles = []
game_over = False

# Functions
def draw_window():
    window.blit(car_image, (car_x, car_y))
    for obstacle in obstacles:
        pygame.draw.rect(window, RED, obstacle)
    pygame.display.update()

def generate_obstacle():
    x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    y = -OBSTACLE_HEIGHT
    obstacles.append(pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def move_obstacles():
    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED

def check_collision():
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)):
            return True
    return False

def reset_game():
    global obstacles, game_over
    obstacles = []
    game_over = False

# Main game loop
while True:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and game_over:
            # Reset the game when a key is pressed after game over
            obstacles = []
            game_over = False
            score = 089
            reset_game()
    
    #background img
    window.blit(background_image, (0, 0))

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Score: " + str(score), True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        window.blit(text, text_rect)
        pygame.display.update()
        continue

    # Generate obstacles
    if random.randint(0, 100) < 2:
         obstacles.append(pygame.Rect(random.randint(0, WIDTH - OBSTACLE_WIDTH), -OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += 5

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED
        # Check if the obstacle has passed the car
        if obstacle.y > HEIGHT:
            calculate_score()
            obstacles.remove(obstacle)

    # Draw the car
    window.blit(car_image, (car_x, car_y))
   
        # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(window, RED, obstacle)

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    # Check for collisions
    if check_collision():
        for obstacle in obstacles:
            if obstacle.colliderect(pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)):
                game_over = True


    # Update the window
    draw_window()