"""
Dungeon Explorer

You are a dungeon explorer aiming to find the treasure. Create a game where the
user can navigate through the dungeon to find the treasure using:

'UP', 'DOWN', 'LEFT', 'RIGHT'

Dungeon Key:
"X" = Trap. If user goes to X it is game over
"*" = User
"W" = Wall. User cannot go there
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
    ["X", " ", "T"],
    [" ", "-", " "],
    ["*", " ", " "]
]

player_position = [0, 0]
treasure_position = [0, 2]

def print_map():
    for i in range(len(map)):
        for j in range(len(map[0])):
            print(map[i][j], end= " ")
        print()

game_is_done = False
while not game_is_done:
    # handle game input

    # handle update game state

    print_map()    
    break # comment this out when you start developing the game
