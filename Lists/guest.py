import random

# below we are creating an empty list
# 1
guest_list = []

# the while loop below is used to ask users for name of guest
# the guest name will be added to the list using the append word
# it will also ask if there are more names which will be Y for yes and N for no
# if the using inputs N meaning no more names, the loop will end
# after which the guest list will be printed

# 2
while True:
    guest_name = input('Enter your guest name: ')
    guest_list.append(guest_name)

    more_names = input('anymore names? ''Y'' to enter more names, ''N'' to stop: ')
    if guest_name == guest_list:
        print('This name already exists, please type another name')
    # tried to stop same name from appearing twice but failed.
    if more_names == 'N':
        break

print(guest_list)

# below we will print all the names using enumerate to print
# a numbered list.


# 3
for index, guest in enumerate(guest_list):
    print(f'{index}: {guest}')

# below we will ask the user if they want to delete any names using the
# using a while loop

# 4
while True:
    delete_name = str(input('Would you like to remove a name on the list? '))
    guest_list.remove(delete_name)

    if delete_name:
        break

print(guest_list)

# 5
# writing a function to print a numbered guest list using the enumerate
# key word

for number, letter in enumerate(guest_list):
    print(number, letter)

# 6
# we are using the random word to distribute prizes to guest
# we started by importing random at the top of the page

# since we already have a guest list, we created a prize list
prize_list = ['dvd', 'ps5', 'car', 'bicycle', 'food']

# Using input to ask how many prizes there should be
input('how many prizes there should be? ')

# created guest-selected and prize-selected variables
#  to use the random.choice word


prize_selected = random.choice(prize_list)

guest_selected = random.choice(guest_list)

# if element present then return
# exist otherwise not exist
# if guest_selected in prize_winner:
#     print("exist")
# else:
#     print("not exist")

# we print the name of the user from the list as well as the price they have won.
print(f'Dear {guest_selected}, you have won {prize_selected} as a prize. ')

# 7
# printing the total number of guests
for number, letter in enumerate(guest_list):
    print(number, letter)
print(guest_list)

# All guest as a numbered list


# names of the guest who will be given a prize
# i created a variable called prize winners and stored the winners in it
# then i printed the winners

prize_winners = guest_selected
print(f'this is the list of winner [{prize_winners}]')
