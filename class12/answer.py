import pygame
from pygame.time import Clock
"""
Background on Clock.tick()

The frame rate or refresh rate is the number of pictures that the program draws per second, and is measured in FPS or frames per second. (On computer monitors, the common name for FPS is hertz. Many monitors have a frame rate of 60 hertz, or 60 frames per second.) A low frame rate in video games can make the game look choppy or jumpy. If the program has too much code to run to draw to the screen frequently enough, then the FPS goes down. But the games in this book are simple enough that this won’t be issue even on old computers.

A pygame.time.Clock object can help us make sure our program runs at a certain maximum FPS. This Clock object will ensure that our game programs don’t run too fast by putting in small pauses on each iteration of the game loop. If we didn’t have these pauses, our game program would run as fast as the computer could run it. This is often too fast for the player, and as computers get faster they would run the game faster too. A call to the tick() method of a Clock object in the game loop can make sure the game runs at the same speed no matter how fast of a computer it runs on. 

For this lesson we now want to move towards creating a jumping game similar to the google dino run game:
https://trex-runner.com/

We will need to use clock.tick(FPS) to make sure that the animation doesn't happen too fast for the human eyes to see.


1. To start we need to draw a rectangle for our foreground to represent the ground.
Hint: recommended rectangle size would be (0, 400, 700, 500) ie x: 0, y: 400, width: 700, height: 500

2. Position the character so that it is on top of the rectangel
Hint: recommended character position would be x: 0, y: 300

3. Draw our enemey (tree.png)
- load it in
- scale it to (50, 100)
- draw it at the position initial (450, 300)

4. Animate it moving from right to left
- step size will be x -= 5

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
    pygame.draw.rect(screen, GREEN, (0, 400, 700, 500))
    screen.blit(tree, (tree_x, tree_y))
    pygame.display.update()