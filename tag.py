import pygame, sys
from pygame.locals import *

class Player():

    def __init__(self, number, startX, startY, velocity):
        self.X = startX
        self.Y = startY
        self.velocity = velocity
        self.startX = startX
        self.startY = startY
        self.number = number
        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False

def MovePlayer(player):
    if player.rightPressed:
        player.X += player.velocity
    if player.leftPressed:
        player.X -= player.velocity
    if player.upPressed:
        player.Y -= player.velocity
    if player.downPressed:
        player.Y += player.velocity
    
    if player.Y + PIXEL > WINDOW_HEIGHT:
        player.Y = 0
    if player.X + PIXEL > WINDOW_WIDTH:
        player.X = 0
    if player.Y < 0:
        player.Y = WINDOW_HEIGHT - PIXEL
    if player.X < 0:
        player.X = WINDOW_WIDTH - PIXEL
    

def CenterText(string, centerX, centerY):
    text = FONT.render(string, True, GREEN)
    textRect = text.get_rect()
    textRect.center = (centerX, centerY)
    return text, textRect

def Main(velocity, time, pixel, width, height):
    # Setup
    pygame.init()
    global BACKGROUND, RED, BLUE, GRAY, GREEN, BLACK, WINDOW_WIDTH, WINDOW_HEIGHT, PIXEL, WINDOW, CLOCK, FONT
    BACKGROUND = (255, 255, 255)
    RED = (255, 30, 70)
    BLUE = (10, 20, 200)
    GRAY = (211,211,211)
    GREEN = (50, 230, 40)
    BLACK = (0,0,0)
    WINDOW_WIDTH = int(width)
    WINDOW_HEIGHT = int(height)
    PIXEL = int(pixel)
    VELOCITY = int(velocity)
    TIME = int(time)
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font('freesansbold.ttf', 24)
    pygame.display.set_caption('Tag')
            
    # Main game loop
    player1 = Player(1, PIXEL, PIXEL, VELOCITY)
    player2 = Player(2, WINDOW_WIDTH-2*PIXEL, WINDOW_HEIGHT-2*PIXEL, VELOCITY)
    startTicks = pygame.time.get_ticks()
    PLAYING = True
    COUNTING = True
    while True:
        
        CLOCK.tick(60)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_d:
                        player1.rightPressed = True
                    if event.key == K_a:
                        player1.leftPressed = True
                    if event.key == K_w:
                        player1.upPressed = True
                    if event.key == K_s:
                        player1.downPressed = True
                elif event.type == pygame.KEYUP:
                    if event.key == K_d:
                        player1.rightPressed = False
                    if event.key == K_a:
                        player1.leftPressed = False
                    if event.key == K_w:
                        player1.upPressed = False
                    if event.key == K_s:
                        player1.downPressed = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RIGHT:
                        player2.rightPressed = True
                    if event.key == K_LEFT:
                        player2.leftPressed = True
                    if event.key == K_UP:
                        player2.upPressed = True
                    if event.key == K_DOWN:
                        player2.downPressed = True
                elif event.type == pygame.KEYUP:
                    if event.key == K_RIGHT:
                        player2.rightPressed = False
                    if event.key == K_LEFT:
                        player2.leftPressed = False
                    if event.key == K_UP:
                        player2.upPressed = False
                    if event.key == K_DOWN:
                        player2.downPressed = False
                
                    
            else:
                # Check for game reset
                if event.type == pygame.MOUSEBUTTONDOWN:
                    PLAYING = True
                    COUNTING = True
                    startTicks = pygame.time.get_ticks()
                    player1 = Player(1, player1.startX, player1.startY, VELOCITY)
                    player2 = Player(2, player2.startX, player2.startY, VELOCITY)
                
        if PLAYING:
            # Process game 
            MovePlayer(player1)
            MovePlayer(player2)
            player1Rect = pygame.Rect(player1.X, player1.Y, PIXEL, PIXEL)
            player2Rect = pygame.Rect(player2.X, player2.Y, PIXEL, PIXEL)
            # Check for game over
            seconds = TIME - ((pygame.time.get_ticks()-startTicks) / 1000)
            secondsText, secondsTextRect = CenterText('{0:.3f}'.format(seconds), WINDOW_WIDTH // 2, 20)
            if seconds < 0:
                secondsText, secondsTextRect = CenterText('0.000', WINDOW_WIDTH // 2, 20)
                COUNTING = False
                PLAYING = False
            elif ((player1.X + PIXEL) > player2.X and player1.X < (player2.X + PIXEL) and
                (player1.Y + PIXEL) > player2.Y and player1.Y < (player2.Y + PIXEL)):
                PLAYING = False

            # Render game
            WINDOW.fill(BACKGROUND)
            WINDOW.blit(secondsText, secondsTextRect)
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

if __name__ == '__main__':
    Main(3, 10, 20, 400, 400)

# # Start screen loop
    # starting = True
    # while starting:
    #     for event in pygame.event.get() :
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             starting = False
    #     text, textRect = CenterText("Click anywhere to start!", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    #     WINDOW.fill(BACKGROUND)
    #     WINDOW.blit(text, textRect)
    #     pygame.display.update()
    