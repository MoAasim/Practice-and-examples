# Ludo dicing game

import random
import time


def getDiceValue():
    val = random.randint(1,6)
    return val


print("Want to try dice (Y/N) ?")
choice = input()
if choice.lower() == 'y':
    print("Rolling the dice...")
    time.sleep(3)
    print("Your score is:", getDiceValue())
    time.sleep(1)
    print("Thank you. It was a good game")
else:
    print("You choose not to roll dice. Thank you")


# Default value for get function
mapping = {
    'one': 1,
    'two': 2,
    'three': 3
}

print(mapping.get('eee', "Default value"))