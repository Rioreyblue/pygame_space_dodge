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