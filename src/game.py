import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.image.load("images/bg.jpeg")

def main():
    run = True

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break;
            
    pygame.quit()
