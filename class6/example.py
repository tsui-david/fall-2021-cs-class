print(">>>> YOU ARE RUNNING THE EXAMPLE FILE. SWITCH TO main.py in .replit")

## Class Exercise
## Draw a line and move it around according to user's command
import pygame
pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
size = (700,500)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

MOVE_PIXELS = 10
start = [10, 10]
end = [50, 50]

i = 0
while not done:
    # print("NEW FRAME", i)
    i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            start[0] -= MOVE_PIXELS
            end[0] -= MOVE_PIXELS
          if event.key == pygame.K_RIGHT:
            start[0] += MOVE_PIXELS
            end[0] += MOVE_PIXELS
          if event.key == pygame.K_UP:
            start[1] -= MOVE_PIXELS
            end[1] -= MOVE_PIXELS
          if event.key == pygame.K_DOWN:
            start[1] += MOVE_PIXELS
            end[1] += MOVE_PIXELS

    screen.fill(WHITE)

    pygame.draw.line(screen, GREEN, start, end, 5)
    pygame.display.flip()

    clock.tick(60)
