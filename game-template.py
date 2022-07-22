import pygame, sys
from pygame.locals import *
pygame.init()

# Colors
BACKGROUND = (255, 255, 255)

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    
    # Process game elements
    WINDOW.fill(BACKGROUND)

    # Render elements of the game
    pygame.display.update()
    