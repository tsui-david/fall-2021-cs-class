import pygame
"""
Exercise 1.

create a function called 'draw_person'
Our game will use this function to draw a person.

In order for us to draw, we will need to pass in an argument 'screen'
which will represent the 

To draw a person we will need:
- ellipse as the head 
- two lines as the legs
- two lines as the arms
- one line as the body
"""


"""
Exercise 2.
Modify the same function.
This time, we want the function to take in 'x' and 'y' position.
Depending on the 'x' and 'y' argument, we want to change where the stickfigure is drawn.
"""

"""
Exercise 3.
Time to test it out in our game!
Plug our function into the code and see if you can move your avatar with key presses
"""

"""
Exercise 4.
We want to draw ANOTHER person (so 2 people in total now)
This person will reuse the same function but its coordinates will be offset by +10 x and +10 y

Create new coordinates: person_2_x and person_2_y to represent the new person's coordinates
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

        screen.fill(WHITE)
        # add your function here!
        pygame.display.flip()
