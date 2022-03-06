import pygame
from pygame.time import Clock
"""
Collision Detection

1. Write a function to handle when two rectangles collide (OR maybe someone might have wrote it? *wink wink wink*)

2. Add the has_surfaces_collided into the game loop and test to see if the objects collide by printing "YOU DIED" to console

3. Pause the game (But don't exit the game) when the has_surfaces_collided is True
*Hint*: We exit the game by breaking outside of the while loop. 
To "pause" - you simply don't update any x, y coordinates even if users have added inputs

"""

# ----------Update code here below here (Uncomment everything below this line using 'cmd+/' or 'ctrl+/')-----------
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Run Game")

# Loop until the user clicks the close button.
done = False

# Current position
person_1_x = 0
person_1_y = 300
step_size = 10

tree_x = 450
tree_y = 300

MAX_FPS = 40
# Load your image in
bg_image = pygame.image.load("assets/backgroundCastles.png")
bg_image = pygame.transform.scale(bg_image, size)
avatar = pygame.image.load("assets/character_robot_walk0.png")
avatar = pygame.transform.scale(avatar, [80, 100])

tree = pygame.image.load("assets/tree.png")
tree = pygame.transform.scale(tree, [50, 100])

clock = Clock()
user_died = False
while not done:
    clock.tick(MAX_FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                person_1_x -= step_size
            elif event.key == pygame.K_RIGHT:
                person_1_x += step_size
            elif event.key == pygame.K_UP:
                person_1_y -= step_size
            elif event.key == pygame.K_DOWN:
                person_1_y += step_size
    tree_x -= 5
    screen.blit(bg_image, (0, 0))
    screen.blit(avatar, (person_1_x, person_1_y))
    screen.blit(tree, (tree_x, tree_y))
    pygame.draw.rect(screen, GREEN, (0, 400, 700, 500))
    pygame.display.update()
    
