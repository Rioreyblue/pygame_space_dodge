import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(WIN, BG, player1, player2):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, (255, 0, 0), player1)
    pygame.draw.rect(WIN, (0, 255, 0), player2)
    pygame.display.update()

def run_game():
    pygame.init()
    
    # Set up display and load assets AFTER pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodge")
    BG = pygame.transform.scale(pygame.image.load("images/bg.jpeg"), (WIDTH, HEIGHT))

    #for time display
    start_time = time.time()
    elapsed_time = 0
    
    #for lock framerate
    clock = pygame.time.Clock()
    
    #player
    player1 = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(800, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    run = True
    while run:
        clock.tick(60)  # Cap frame rate at 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x - PLAYER_VEL >=0:
            player1.x -= PLAYER_VEL
        if keys[pygame.K_d] and player1.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player1.x += PLAYER_VEL
            
        if keys[pygame.K_LEFT] and player2.x - PLAYER_VEL >=0:
            player2.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player2.x + PLAYER_VEL + PLAYER_WIDTH <=WIDTH:
            player2.x += PLAYER_VEL

        draw(WIN, BG, player1, player2)

    pygame.quit()