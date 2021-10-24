"""
Exercise 2.
Modify the camel game.


Objective 1:
Give users the ability to select game difficulty at the beginning:

1. EASY: max thirst = 20, max tiredness = 20
2. MEDIUM: same as current
3. HARD: max thirst = 5 max tiredness = 5


Objective 2:
Add a "Play again?" functionality that allows the user to play the game all over again.


Objective 3:
Print a picture of where you are relative to the natives and finish line
When user displays status

Example:

____x_____*__________FINISH


Hints:
- You can print multiple times with the following command:
    Ex:
    print('_'*12) which will print '_' 12 times
- break each section down and store as a variable:
    - distance the natives have traveled from start
    - distance you have traveled from natives
    - distance of finish line from you

- remember that strings can be joined together!
    Ex:
    a = 'alice'
    b = 'bob'
    print(a+' '+b) outputs 'alice bob'
- if you are printing the full distance, it might go out of the screen.
  we can scale everything down by dividing by 2

    Ex:
    print('_'*(dist//2))
"""

import random

MAX_THIRST = 10
MAX_TIREDNESS = 10
MAX_DIST_TRAVEL = 50

MODERATE_MIN_TRAVEL = 7
MODERATE_MAX_TRAVEL = 10

FAST_MIN_TRAVEL = 10
FAST_MAX_TRAVEL = 25

MODERATE_TIREDNESS_COST = 1
MODERATE_THIRST_COST = 1

FAST_TIREDNESS_COST = 3
FAST_THIRST_COST = 3

NATIVES_MIN_TRAVEL = 5
NATIVES_MAX_TRAVEL = 15

# status variables
status_miles_traveled = 0
status_thirst = 0
status_tiredness = 0
status_canteen = 5
status_natives_miles_traveled = -20

# prompts
camel_prompt = """
==================================
                  ,,__
        ..  ..   / o._)                   .---.
       /--'/--\  \-'||        .----.    .'     '.
      /        \_/ / |      .'      '..'         '-.
    .'\  \__\  __.'.'     .'          i-._
      )\ |  )\ |      _.'
     // \\ // \\
    ||_  \\|_  \\_
    '--' '--'' '--'

Welcome to Camels Game!

You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives.

You lose:
- if the natives catch up to you
- your camel tiredness >= {}
- your camel thirst >= {}

You win:
- if you survive and travel >= {}
==================================""".format(
    MAX_TIREDNESS,
    MAX_THIRST,
    MAX_DIST_TRAVEL
)


is_gameover = False

while not is_gameover:
    choices_prompt = """
    A. Drink from your canteen. [Thirst = 0, Canteen -= 1]
    B. Ahead moderate speed.    [Miles += {moderate_min}~{moderate_max}, Thirst += {moderate_thirst}, Tirdeness += {moderate_tiredness}]
    C. Ahead full speed.        [Miles += {fast_min}~{fast_max}, Thirst += {fast_thirst}, Tiredness += {fast_tiredness}]
    D. Stop and rest.           [Tiredness = 0]
    E. Status check.
    Q. Quit.

    Natives Miles += {native_min}~{native_max} For every choice except E. and Q.
    
    You will lose if:
    - your camel thirst >= {thirst_level}
    - your came tiredness >= {tired_level}
    - natives travel >= your travel
    You win if you travel >= {max_travel}
    """.format(
        moderate_min=MODERATE_MIN_TRAVEL,
        moderate_max=MODERATE_MAX_TRAVEL,
        moderate_tiredness=MODERATE_TIREDNESS_COST,
        moderate_thirst=MODERATE_THIRST_COST,
        fast_min=FAST_MIN_TRAVEL,
        fast_max=FAST_MAX_TRAVEL,
        fast_thirst=FAST_THIRST_COST,
        fast_tiredness=FAST_TIREDNESS_COST,
        native_min=NATIVES_MIN_TRAVEL,
        native_max=NATIVES_MAX_TRAVEL,
        thirst_level=MAX_THIRST,
        tired_level=MAX_TIREDNESS,
        max_travel=MAX_DIST_TRAVEL
    )

    status = """
    -------
    CURRENT STATUS:
    * Miles Traveled: {}
    * Thirst Level: {}
    * Canteen Level: {} 
    * Tiredness Level: {}

    The natives are currently {} miles behind you!
    -------
    """.format(
        status_miles_traveled,
        status_thirst,
        status_canteen,
        status_tiredness,
        status_miles_traveled - status_natives_miles_traveled
    )

    

    user_choice = input(choices_prompt).upper()
    should_incur_penalty = True

    if user_choice == 'A':
        if status_canteen > 0 :
            status_thirst = 0
            status_canteen -= 1
        else:
            should_incur_penalty = False
            print('No more canteens available...')
    elif user_choice == 'B':
        speed = random.randint(MODERATE_MIN_TRAVEL, MODERATE_MAX_TRAVEL)
        status_miles_traveled += speed
        status_thirst += MODERATE_THIRST_COST
        status_tiredness += MODERATE_TIREDNESS_COST
    elif user_choice == 'C':
        speed = random.randint(FAST_MIN_TRAVEL, FAST_MAX_TRAVEL)
        status_miles_traveled += speed
        status_thirst += FAST_THIRST_COST
        status_tiredness += FAST_TIREDNESS_COST
    elif user_choice == 'D':
        status_tiredness = 0
    elif user_choice == 'E':
        print(status)
        should_incur_penalty = False
    elif user_choice == 'Q':
        break
    
    if should_incur_penalty:
        natives_speed = random.randint(NATIVES_MIN_TRAVEL, NATIVES_MAX_TRAVEL)
        status_natives_miles_traveled += natives_speed

        if status_natives_miles_traveled >= status_miles_traveled:
            print("The natives have caught up!! You lose")
            is_gameover = True
        elif status_tiredness >= MAX_TIREDNESS:
            print("Your camel has died from exhaustion!! You lose")
            is_gameover = True 
        elif status_thirst >= MAX_THIRST:
            print("Your camel has died of thirst!! You lose")
            is_gameover = True
        elif status_miles_traveled >= MAX_DIST_TRAVEL:
            print("YOU HAVE WON!!")
            is_gameover = True

print("GAME OVER")

