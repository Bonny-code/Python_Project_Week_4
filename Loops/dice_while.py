import random

want_to_quit = ' '  # empty string means false

while not want_to_quit:
    dice_value = random.randint(1,6)
    print(' You rolled a ' + str(dice_value))
    want_to_quit = input('Press enter to roll again, and any other key to quit')
