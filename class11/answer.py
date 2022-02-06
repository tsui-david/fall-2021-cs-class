import pygame

"""
Exercise 1:
Load in your images from the assets folder.
We will need a background image and a character image.
Take your pick what you would like...

Hint: what is the path to the image?
"""

"""
Exercise 2:
Draw the background image onto the whole screen.
"""

"""
Exercise 3:
Resize the image so that it fits into the screen.
Hint: What is the screen's size? Do we have a variable to represent the screen size?
"""

"""
Exercise 4:
Draw a character image onto the screen.
"""

"""
Exercise 5:
Resize the character so that it is bigger.
You might need to play around with the width and height.. 
"""

"""
Exercise 6:
This might be done by exercise 4 depending on your implementation. 
But we now want to draw it to wherever the player moves it.

Hint:
Do we have variables to represent the coordinates?
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
pygame.display.set_caption("Stickfigure Game")

# Loop until the user clicks the close button.
done = False

# Current position
person_1_x = 10
person_1_y = 10
step_size = 10

bg_image = pygame.image.load(assets/backgroundCastles.png)

# Load your image in
bg_image = pygame.image.load("assets/backgroundCastles.png")
bg_image = pygame.transform.scale(bg_image, size)
avatar = pygame.image.load("assets/character_robot_walk0.png")
avatar = pygame.transform.scale(avatar, [80, 100])

while not done:
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

        screen.blit(bg_image, (0, 0))
        screen.blit(avatar, (person_1_x, person_1_y))
        pygame.display.flip()
