import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Arithmetic Operations")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont(None, 48)

# Text input variables
input_text = ''
input_rect = pygame.Rect(50, 50, 300, 50)
is_input_active = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                is_input_active = True
            else:
                is_input_active = False
        elif event.type == pygame.KEYDOWN:
            if is_input_active:
                if event.key == pygame.K_RETURN:
                    try:
                        result = eval(input_text)
                        input_text = str(result)
                    except:
                        input_text = 'Error'
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the input box
    pygame.draw.rect(screen, BLACK, input_rect, 2)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Update the display
    pygame.display.flip()
pygame.exit()
sys.exit()