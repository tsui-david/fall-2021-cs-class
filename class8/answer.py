"""
Dungeon Explorer

You are a dungeon explorer aiming to find the treasure. Create a game where the
user can navigate through the dungeon to find the treasure using:

'UP', 'DOWN', 'LEFT', 'RIGHT'

Dungeon Key:
"X" = Trap. If user goes to X it is game over
"*" = User
"-" = Wall. User cannot go there
"T" = Treasure. User wins
" " = Blank. Empty space

The dungeon map looks like:

[
 ["X"," ", "T"],
 [" ","-", " "],
 ["*"," ", " "]
]

Example of play through:

Make a choice: "UP", "LEFT", "DOWN", "RIGHT": RIGHT
[
 ["X"," ", "T"],
 [" ","-", " "],
 [" ","*", " "]
]

Make a choice: "UP", "LEFT", "DOWN", "RIGHT": UP
You've hit a wall...
[
 ["X"," ", "T"],
 [" ","-", " "],
 [" ","*", " "]
]

Make a choice: "UP", "LEFT", "DOWN", "RIGHT": RIGHT
[
 ["X"," ", "T"],
 [" ","-", " "],
 [" "," ", "*"]
]

Make a choice: "UP", "LEFT", "DOWN", "RIGHT": UP
[
 ["X"," ", "T"],
 [" ","-", "*"],
 [" "," ", " "]
]

Make a choice: "UP", "LEFT", "DOWN", "RIGHT": UP
You win!
[
 ["X"," ", "*"],
 [" ","-", " "],
 [" "," ", " "]
]
""
"""

from helper import (
    print_game_over,
    print_game_wall,
    print_game_win
)

map = [
    ["X", " ", " ", " "], # 0
    [" ", " ", "-", " "], # 1
    ["X", " ", "X", " "], # 2
    ["*", " ", "-", "T"]  # 3
  #.  0.   1.   2.   3
]

player_position = [3, 0]

def print_map():
    for r in map:
      for c in r:
          print(c, end= " ")
      print()

game_is_done = False
while not game_is_done:
    direction = input('What direction do you want to go? U, D, L, R ')
    player_r = player_position[0]
    player_c = player_position[1]

    if direction == 'R':
      new_player_r = player_r
      new_player_c = player_c + 1
    if direction == 'U':
      new_player_r = player_r - 1
      new_player_c = player_c 
    if direction == 'D':
      new_player_r = player_r + 1
      new_player_c = player_c
    if direction == 'L':
      new_player_r = player_r
      new_player_c = player_c - 1

    # handle out of bounds

    if new_player_c >= len(map[0]) or new_player_r >= len(map):
      print("OUT OF BOUNDS!")
      continue
    
    if new_player_c < 0 or new_player_r < 0:
      print("OUT OF BOUNDS!")
      continue

    # handle update game state
    if map[new_player_r][new_player_c] == 'T':
      print_game_win()
      break
    if map[new_player_r][new_player_c] == 'X':
      print_game_over()
      break
    if map[new_player_r][new_player_c] == '-':
      print_game_wall()
      continue

    print('next position will be: ', map[new_player_r][new_player_c])
    map[new_player_r][new_player_c] = "*"
    # clean up
    map[player_r][player_c] = " "
    print_map() 
    player_position = [new_player_r, new_player_c]






# print_map()
# new_player_r =player_r
# new_player_c = player_c + 1
# map[new_player_r][new_player_c] = "*"

# # clean up

# map[player_r][player_c] = " "
# print('after moving right')
# print_map()

