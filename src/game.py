import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800

def run_game():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodge")

    # Load image inside the function after initializing display
    bg = pygame.image.load("images/bg.jpeg")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        win.blit(bg, (0, 0))
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
