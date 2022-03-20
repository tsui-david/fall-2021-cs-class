"""
Step 1.
line 69 and 70: cur_tree_x and cur_tree_y will need to be removed.
Instead, create an array called trees.
This will hold hardcoded values of [[450, 350], [650, 350], [850, 350], [1000, 350]]

Step 2.
Replace all cur_tree_x and cur_tree_y instances in the rest of the code with a for loop of tree coordinates.
Modify the blit to handle the tree coordinates instead.
"""

import pygame
import math
from pygame.time import Clock

def get_score_string_from_raw_score(raw_score):
    return "Score: "+str(math.floor(raw_score/10))

# --- Constants - constant variables do not change and are usually capitalized ----

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# tree values
MAX_NUM_TREES = 5
TREE_STARTING_X = 450
TREE_STARTING_Y = 350
SECONDS_PER_TREE = 5

# player values
PLAYER_STARTING_X = 10
PLAYER_STARTING_Y = 350
MAX_JUMP_HEIGHT = 120
JUMP_SPEED = 10

# screen values
MAX_FPS = 40
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Load your image in
bg_image = pygame.image.load("assets/backgroundCastles.png")
bg_image = pygame.transform.scale(bg_image, [700, 500])
player_image = pygame.image.load("assets/character_robot_walk0.png")
player_image = pygame.transform.scale(player_image, [40, 50])

tree_image = pygame.image.load("assets/tree.png")
tree_image = pygame.transform.scale(tree_image, [25, 50])

# ----------Update code here below here (Uncomment everything below this line using 'cmd+/' or 'ctrl+/')-----------
pygame.init()
 
# Set the width and height of the screen [width, height]
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Run Game")

# Loop until the user clicks the close button.
done = False

# Current player position
cur_player_x = PLAYER_STARTING_X
cur_player_y = PLAYER_STARTING_Y


# Jump vars
cur_jump_count = 0
has_jumped = False

# Trees
cur_tree_x = TREE_STARTING_X
cur_tree_y = TREE_STARTING_Y

# Time
clock = Clock()
user_died = False

# Score
raw_score = 0

# Initialize a font
score_font = pygame.font.SysFont("calibri", 30)


# game loops until done == False
while not done:
    # syncs game with FPS
    clock.tick(MAX_FPS)

    # watch for spacebar press event or close game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not has_jumped:
              has_jumped = True

    if user_died:
        # if user died, we don't move to code that updates
        continue

    # user has not died yet, we keep going!

    if has_jumped:
        if cur_jump_count < MAX_JUMP_HEIGHT:
            # player going up towards teh jump apex
            cur_player_y -= JUMP_SPEED
            cur_jump_count += JUMP_SPEED
        elif cur_jump_count >= (MAX_JUMP_HEIGHT * 2):
            # player has finished jumping and we need to reset to original player position
            cur_player_y = PLAYER_STARTING_Y
            # cur_player_x = PLAYER_STARTING_X
            cur_jump_count = 0
            has_jumped = False
        elif cur_jump_count >= MAX_JUMP_HEIGHT:
            # player coming down from the jump apex
            cur_player_y += (JUMP_SPEED * .8)
            cur_jump_count += (JUMP_SPEED * .8) 

    cur_tree_x -= 8
    screen.blit(bg_image, (0, 0))
    user_surface = screen.blit(player_image, (cur_player_x, cur_player_y))
    tree_surface = screen.blit(tree_image, (cur_tree_x, cur_tree_y))

    if pygame.Rect.colliderect(user_surface, tree_surface):
        user_died = True
  
    raw_score += 1
    score_str = get_score_string_from_raw_score(raw_score)
    score_img = score_font.render(score_str, True, RED)
    screen.blit(score_img, (20, 20))
 
    pygame.draw.rect(screen, GREEN, (0, 400, 700, 500))
    pygame.display.update()


