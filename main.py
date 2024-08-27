import pygame
from constants import *

# Initialize pygame
pygame.init()

# Create a screen surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Fill the screen with black color
    black = (0, 0, 0)  # RGB values for black
    screen.fill(black)

    # Update the display
    pygame.display.flip()

    # Simple event loop to keep the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
