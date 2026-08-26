import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800

def run_game():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodge")

    # Load image inside the function after initializing display
    BG = pygame.transform.scale(pygame.image.load("images/bg.jpeg"), (WIDTH, HEIGHT))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        WIN.blit(BG, (0, 0))
        pygame.display.update()

    pygame.quit()





# import pygame
# import time
# import random

# WIDTH, HEIGHT = 1000, 800
# WIN = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("Space Dodge")

# BG = pygame.image.load("images/bg.jpeg")

# def draw():
#     WIN.blit(BG,())

# def main():
#     run_game = True

#     while run_game:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run_game = False
#                 break;
            
#     pygame.quit()
