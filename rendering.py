import pygame, sys
from pygame.locals import *
pygame.init()

# Colors
BACKGROUND = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)

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
    rectangle1 = pygame.Rect(10, 10, 10, 50)
    rectangle2 = pygame.Rect(380, 100, 10, 50)
    

    # Render elements of the game
    
    pygame.draw.rect(WINDOW, RED, rectangle1)
    pygame.draw.rect(WINDOW, GREEN, rectangle2)
    pygame.draw.circle(WINDOW, BLUE, (50, 50), 5)
    pygame.draw.line(WINDOW, BLUE, (200, 0), (200, 380), 3)
    pygame.display.update()
    