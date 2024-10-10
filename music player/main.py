import pygame
# Initialize Pygame
pygame.init()

# Set up the screen (not needed for audio)
width, height=800,600
screen = pygame.display.set_mode((width, height))
# Create a list of music files to play
music_files = ["Doraemon.mp3", "Chhota-Bheem-Title.mp3", "Ninja-Hattori.mp3"]

background_image = pygame.image.load("dj.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Load the first song in the list
current_song_index = 0
pygame.mixer.music.load(music_files[current_song_index])

# Play the current song
pygame.mixer.music.play()

# Set up fonts for displaying song titles
font = pygame.font.SysFont("Arial", 24)

# Create buttons to skip to the next song and go back to the previous song
next_button_rect = pygame.Rect(650, 200, 100, 50)
next_button_text = font.render("Next", True, (255, 255, 255))
prev_button_rect = pygame.Rect(50, 200, 100, 50)
prev_button_text = font.render("Prev", True, (255, 255, 255))

# Start the game loop
while True:
    # Handle events (including button clicks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # User clicked the "X" button, exit the game
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked the "next" button
            if next_button_rect.collidepoint(event.pos):
                # Stop the currently playing music
                pygame.mixer.music.stop()
                # Go to the next song in the list
                current_song_index += 1
                if current_song_index >= len(music_files):
                    # If we've reached the end of the list, wrap around to the beginning
                    current_song_index = 0
                # Load and play the next song
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
            # Check if the user clicked the "prev" button
            elif prev_button_rect.collidepoint(event.pos):
                # Stop the currently playing music
                pygame.mixer.music.stop()
                # Go to the previous song in the list
                current_song_index -= 1
                if current_song_index < 0:
                   # If we've reached the beginning of the list, wrap around to the end
                    current_song_index = len(music_files) - 1
                # Load and play the previous song
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()

    #background img
    screen.blit(background_image, (0, 0))

   # Draw the buttons and current song title on the screen

    pygame.draw.rect(screen, (255, 0, 0), next_button_rect)
    pygame.draw.rect(screen, (255, 0, 0), prev_button_rect)
    screen.blit(next_button_text, next_button_rect)
    screen.blit(prev_button_text, prev_button_rect)
    current_song_title = font.render(music_files[current_song_index], True, (255, 255, 255))

    screen.blit(current_song_title, (320 - current_song_title.get_width() // 2, 100 - current_song_title.get_height() // 2))

    # Update the screen
    pygame.display.update()
