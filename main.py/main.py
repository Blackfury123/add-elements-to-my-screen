import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("I DO NOT KNOW WHAT TO NAME IT LOLLL!!!!!!!!!!")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a rectangle
rect = pygame.Rect(100, 100, 200, 200)

# Create a font for the text
font = pygame.font.Font(None, 36)

# Create some text
text = font.render("Hello, World!", True, BLACK)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Stop the game loop

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLACK, rect)

    # Draw the text
    screen.blit(text, (100, 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame when the loop ends
pygame.quit()
