import pygame
import time
import random
pygame.font.init() #for font usage of time/elapsed

WIDTH, HEIGHT = 1000, 800
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

FONT = pygame.font.SysFont("poppins", 30) #creating font object

def draw(WIN, BG, player1, player2, elapsed_time):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))
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


    #boulders
    BOULDER_WIDTH = 10
    BOULDER_HEIGHT = 20
    boulder_add_increment = 2000
    boulder_count = 0

    boulder = []


    run = True
    while run:
        #usage 
        # clock.tick(60)  # Cap frame rate at 60 FPS
        boulder_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if boulder_count > boulder_add_increment:
            for _ in range(3):
                boulder_x = random.randint(0,WIDTH - BOULDER_WIDTH)
                boulder = pygame.Rect(boulder_x, - BOULDER_HEIGHT)

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

        draw(WIN, BG, player1, player2, elapsed_time)

    pygame.quit()