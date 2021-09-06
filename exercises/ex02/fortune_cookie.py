"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730530311"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune_one: str = str("You will meet the love of your life today!")
fortune_two: str = str("Your future is bright...")
fortune_three: str = str("Today is your lucky day!")
fortune_four: str = str("You will step on a bug today...")
random: int = int(randint(1, 4))

print("Your fortune cookie says... ")


if random == 1:
    print(fortune_one)

else:
    if random == 2:
        print(fortune_two)

    else: 
        if random == 3:
            print(fortune_three)
        
        else:
            if random == 4:
                print(fortune_four) 

print("Now, go spread positive vibes!")