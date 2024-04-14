# here we are playing the dice game where a random number comes up
# we start by importing the random value from an external library
# we use a variable to store a question asking how many dice to roll
# We then use the for loop to determine the result
# we start by giving it a range between the values of 1 and 6
# then we use random.randint to spin the dice
# at the end we print the value of the random.randint dice

import random

number_of_dice = int(input('How many dice to roll? '))

for dice in range(number_of_dice):
    dice_value = random.randint(1,6)
    print(f'the dice rolld a {dice_value}')

print('That was all')
