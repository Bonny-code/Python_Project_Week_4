
star_id = input('Enter your star ID: ')

while len(star_id) != 8:
    print('Error- A valid starid has 8 characters')
    star_id = input('Please enter your star ID: ')
print(f'Thank you, your star id is {star_id}')
