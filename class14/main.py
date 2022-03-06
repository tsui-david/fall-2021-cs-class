import pygame
from pygame.time import Clock
"""
Implement Jumping
Note: I've resized the tree and avatar because the game difficulty is much harder when the objects are super big.

Let's implement the jumping so the avatar can dodge the tree!

1. Pause the tree from coming left by commenting out the tree_x movement. This will help us test our jump without dying all the time.

2. The jump mechanic will come from when user presses spacebar. Implement the press spacebar trigger and print "I'm jumping!" when user presses spacebar

3. To animate the jump - we will be decreasing the y (because 0 is the highest) and then once it reaches an apex, increase the y.

Initialize the following variables:

has_jumped        # when space is pressed; user can't jump while jumping (boolean)
cur_jump_count    # track the current jump trajectory                    (integer)
max_jump_height   # the apex height                                      (integer)
jump_speed        # the speeed of the ascension/descension               (integer)

!!! I want you guys to initialize some numbers you see fit :) Part of the challenge is tweaking the numbers so that the game is playable

- we need `has_jumped` because we don't want users to jump while they're in the process of animating the jump.
- we will also use `has_jumped` to know when we are still jumping so we can calculate the jump coord
- how do we know if we're ascending / descending? we can use `cur_jump_count` and `max_jump_height` to tell
- if cur_jump_count < max_jump_height => we are ascending
- if cur_jump_count >= max_jump_height => we are descending
- if cur_jump_count >= (max_jump_height * 2) => we are done with jumping

4. implement the `has_jumped` set to true when user presses spacebar. 
5. implement ascension (remember to test!)
- player_y decrease
- cur_jump_count increase

6. implement descension
- player_y increase
- cur_jump_count increase

7. implement resetting from finishing a jump
- cur_jump_count = 0
- player_y = 350

8. you will notice that the game is still pretty hard. that is because our descension speed is pretty fast. slow down the descension speed by a factor of 0.5 - 0.9 

9. uncomment the tree moving left and try adjusting the variables to test the game!

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
person_1_x = 10
person_1_y = 350
step_size = 10

tree_x = 450
tree_y = 350

MAX_FPS = 40
# Load your image in
bg_image = pygame.image.load("assets/backgroundCastles.png")
bg_image = pygame.transform.scale(bg_image, size)
avatar = pygame.image.load("assets/character_robot_walk0.png")
avatar = pygame.transform.scale(avatar, [40, 50])

tree = pygame.image.load("assets/tree.png")
tree = pygame.transform.scale(tree, [25, 50])

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

    if not user_died:
      tree_x -= 5
      screen.blit(bg_image, (0, 0))
      user_surface = screen.blit(avatar, (person_1_x, person_1_y))
      tree_surface = screen.blit(tree, (tree_x, tree_y))

      if pygame.Rect.colliderect(user_surface, tree_surface):
          user_died = True

    
  
    pygame.draw.rect(screen, GREEN, (0, 400, 700, 500))
    pygame.display.update()