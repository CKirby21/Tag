import pygame, sys
from pygame.locals import *
pygame.init()

# Colors
BACKGROUND = (255, 255, 255)
CHARACTER = (255, 30, 70)

# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

characterX = 10
characterY = 30
characterWidth = 20
characterHeight = 20
characterVelocity = 5

# Main game loop
while True :
    # Get inputs
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        pressed = pygame.key.get_pressed()
        if (pressed[K_RIGHT] or pressed[K_d]):
            characterX += characterVelocity
        if (pressed[K_LEFT] or pressed[K_a]):
            characterX -= characterVelocity
        if (pressed[K_UP] or pressed[K_w]):
            characterY -= characterVelocity
        if (pressed[K_DOWN] or pressed[K_s]):
            characterY += characterVelocity

        if event.type == pygame.KEYDOWN and event.key == K_r:
            characterX = 10
            characterY = 30
        if event.type == pygame.KEYUP and event.key == K_r :
            characterX = 340
            characterY = 200
            
    
    # Process game elements
    WINDOW.fill(BACKGROUND)
    character = pygame.Rect(characterX, characterY, characterWidth, characterHeight)

    # Render elements of the game
    pygame.draw.rect(WINDOW, CHARACTER, character)
    pygame.display.update()
    