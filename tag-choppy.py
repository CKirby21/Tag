import pygame, sys
from pygame.locals import *

class Player():

    def __init__(self, number, startX, startY):
        self.X = startX
        self.Y = startY
        self.velocity = 5
        self.startX = startX
        self.startY = startY
        self.number = number
        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False

def MovePlayer(player, pressed):
    playerVelocity = player.velocity
    if player.number == 1:
        if pressed[K_d]:
            player.X += playerVelocity
        if pressed[K_a]:
            player.X -= playerVelocity
        if pressed[K_w]:
            player.Y -= playerVelocity
        if pressed[K_s]:
            player.Y += playerVelocity
    elif player.number == 2:
        if pressed[K_l]:
            player.X += playerVelocity
        if pressed[K_j]:
            player.X -= playerVelocity
        if pressed[K_i]:
            player.Y -= playerVelocity
        if pressed[K_k]:
            player.Y += playerVelocity

def TeleportPlayer(player):
    global PIXEL
    global WINDOW_HEIGHT
    global WINDOW_WIDTH
    if player.Y + PIXEL > WINDOW_HEIGHT:
        player.Y = 0
    if player.X + PIXEL > WINDOW_WIDTH:
        player.X = 0
    if player.Y < 0:
        player.Y = WINDOW_HEIGHT - PIXEL
    if player.X < 0:
        player.X = WINDOW_WIDTH - PIXEL

def ResetPlayer(player):
    player.X = player.startX
    player.Y = player.startY

def CenterText(string, centerX, centerY):
    text = FONT.render(string, True, GREEN)
    textRect = text.get_rect()
    textRect.center = (centerX, centerY)
    return text, textRect


# Setup
pygame.init()
BACKGROUND = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GRAY = (211,211,211)
GREEN = (50, 230, 40)
BLACK = (0,0,0)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
PIXEL = 20
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font('freesansbold.ttf', 24)
pygame.display.set_caption('Tag')

player1 = Player(1, 20, 20)
player2 = Player(2, 360, 360)

# Start screen loop
starting = True
while starting:
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            starting = False
    text, textRect = CenterText("Click anywhere to start!", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    WINDOW.fill(BACKGROUND)
    WINDOW.blit(text, textRect)
    pygame.display.update()
    
# Main game loop
startTicks = pygame.time.get_ticks()
PLAYING = True
COUNTING = True
while True:

    # Check for game over
    seconds = (10000 - (pygame.time.get_ticks()-startTicks)) / 1000
    if seconds < 0 and PLAYING:
        COUNTING = False
        PLAYING = False
    elif ((player1.X + PIXEL) > player2.X and player1.X < (player2.X + PIXEL) and
          (player1.Y + PIXEL) > player2.Y and player1.Y < (player2.Y + PIXEL)):
        PLAYING = False

    # Get inputs
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pressed = pygame.key.get_pressed()
        if PLAYING:
            MovePlayer(player1, pressed)
            MovePlayer(player2, pressed)
        else:
            # Check for game reset
            if event.type == pygame.MOUSEBUTTONDOWN:
                PLAYING = True
                COUNTING = True
                startTicks = pygame.time.get_ticks()
                ResetPlayer(player1)
                ResetPlayer(player2)
            
    if PLAYING:
        # Process game 
        TeleportPlayer(player1)
        TeleportPlayer(player2)
        player1Rect = pygame.Rect(player1.X, player1.Y, PIXEL, PIXEL)
        player2Rect = pygame.Rect(player2.X, player2.Y, PIXEL, PIXEL)
        text, textRect = CenterText(str(seconds), WINDOW_WIDTH // 2, 20)

        # Render game
        WINDOW.fill(BACKGROUND)
        WINDOW.blit(text, textRect)
        pygame.draw.rect(WINDOW, RED, player1Rect)
        pygame.draw.rect(WINDOW, BLUE, player2Rect)
    else:
        # Process game over
        if COUNTING: sentence = 'Player 1 has caught Player 2!'
        else: sentence = 'Player 2 has evaded Player 1!'
        text, textRect = CenterText(sentence, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Render game over
        WINDOW.blit(text, textRect)

    pygame.display.update()
    