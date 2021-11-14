## Class Exercise
## Draw a RED RECTANGLE and move it around according to user's command
## Move by pressing W, A, S, D to move 
## W = up
## A = left
## S = right
## D = down
## space = change color to GREEN (press space again will change back to RED)

import pygame
pygame.init()

# setup your colors for RGB
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# setup your screen size
size = (700,500)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

MOVE_PIXELS = 10
start = [10, 10]
end = [50, 50]


while not done:
    for event in pygame.event.get():
        # fill in your input actions
        continue
    screen.fill(WHITE)
    pygame.display.flip()

    clock.tick(60)
