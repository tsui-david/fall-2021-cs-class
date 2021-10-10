"""
Exercse 1

Print from 1 to 100
Example:
1
2
3
4
5
...
"""







"""
Exercise 2

Print from 1 to 100, only odd
Example:
1
3
5
7
9
...
"""








"""
Exercise 3

Modify the rock paper scissors program below so that the game will repeatedly
play until users pressed "q" for quit.

Also if the player enters in the incorrect input, the game will repeatedly ask for new input

Challenge: Can you keep track of computer and player points?
Example:
------------ NEW GAME ---------------
Play your move: (rock, paper, scissors, quit)  rock
You played: rock Computer played: scissors
You lose!
------------ NEW GAME ---------------
Play your move: (rock, paper, scissors, quit)  paper
You played: paper Computer played: scissors
You lose!
------------ NEW GAME ---------------
Play your move: (rock, paper, scissors, quit)  quit
The game has ended.
"""
# import random

# WIN = "You win!"
# LOSE = "You lose!"
# TIE = "The game has tied!"

# ROCK = 'rock'
# PAPER = 'paper'
# SCISSORS = 'scissors'
# QUIT = 'quit'

# player_move = ""
# computer_move = ""

# print("------------ NEW GAME ---------------")
# player_move = input("Play your move: (rock, paper, scissors, quit)  ")
# if player_move == ROCK or player_move == PAPER or player_move == SCISSORS or player_move == QUIT:
#     pass
# else:
#     print("You did not have correct move. Try again.")


# computer_move = random.randint(0, 3)
# if computer_move == 0:
#     computer_move = ROCK
# elif computer_move == 1:
#     computer_move = PAPER
# else:
#     computer_move = SCISSORS

# print("You played:", player_move, "Computer played:", computer_move)

# if computer_move == player_move:
#     print(TIE)
# elif computer_move == ROCK and player_move == PAPER:
#     print(WIN)
# elif computer_move == PAPER and player_move == ROCK:
#     print(LOSE)
# elif computer_move == PAPER and player_move == SCISSORS:
#     print(WIN)
# elif computer_move == SCISSORS and player_move == PAPER:
#     print(LOSE)
# elif computer_move == ROCK and player_move == SCISSORS:
#     print(WIN)
# else:
#     print(LOSE)

# print("The game has ended.")