"""
Exercise 1.
Create the camel game.

Give the user the following prompt:

-----------------------
Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives.
-------------------------

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.

Every turn, natives advance 5-15 miles

You lose when any of the conditions happen:
1. tiredness > 20
2. thirst > 10
3. natives miles traveled >= your miles traveled

You win when your miles traveled >= 100
"""
### VVVVVVV MODIFY YOUR CODE BELOW VVVVVV

import random

# thresholds - adjust to make game easier/harder
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

choices_prompt = """
A. Drink from your canteen. [Thirst = 0, Canteen -= 1]
B. Ahead moderate speed.    [Miles += {moderate_min}~{moderate_max}, Thirst += {moderate_thirst}, Tirdeness += {moderate_tiredness}]
C. Ahead full speed.        [Miles += {fast_min}~{fast_max}, Thirst += {fast_thirst}, Tiredness += {fast_tiredness}]
D. Stop and rest.           [Tiredness = 0]
E. Status check.
Q. Quit.

Natives Miles += {native_min}~{native_max} For every choice except E. and Q.
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
    native_max=NATIVES_MAX_TRAVEL
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

# print this only once
print(camel_prompt)

# loop game below
print(status)
print(choices_prompt)
choice = input("Pick your option: ")