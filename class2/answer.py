"""
Exercise 1 rock paper scissors

Example

Player 1, play your move: (rock, paper, scissors) rock
Player 2, play your move: (rock, paper, scissors) paper
Player 2 Wins!

---

Player 1, play your move: (rock, paper, scissors) blah
Player 2, play your move: (rock, paper, scissors) blah
Invalid input

"""
# p1 = input('Player 1, play your move: (rock, paper, scissors) ').lower()
# p2 = input('Player 2, play your move: (rock, paper, scissors) ').lower()

# player_1_wins = "Player 1 Wins!"
# player_2_wins = "Player 2 Wins!"

# if p1 == 'rock' and p2 == 'paper':
#     print(player_2_wins)
# elif p1 == 'paper' and p2 == 'rock':
#     print(player_1_wins)
# elif p1 == 'rock' and p2 == 'scissors':
#     print(player_1_wins)
# elif p1 == 'scissors' and p2 == 'rock':
#     print(player_2_wins)
# elif p1 == 'paper' and p2 == 'scissors':
#     print(player_2_wins)
# elif p1 == 'scissors' and p2 == 'paper':
#     print(player_1_wins)
# else:
#     print('Invalid input')

"""
Exercise 2 Valid Triangle

"""
a = int(input('Enter side A  '))
b = int(input('Enter side B  '))
c = int(input('Enter side C  '))

if a + b < c:
    raise Exception("Invalid triangle, a+b < c")
elif a + c < b:
    raise Exception("Invalid triangle, a+c < b")
elif b + c < a:
    raise Exception("Invalid triangle, b+c < a")

print("Valid Triangle!")