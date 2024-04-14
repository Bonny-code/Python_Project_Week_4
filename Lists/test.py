import random

guest_list = ['joana', 'james', 'john', 'steven', 'ghost']

prize_list = ['dvd', 'ps5', 'car', 'bicycle', 'food']

input('how many prizes there should be ')

prize_selected = random.choice(prize_list)

guest_selected = random.choice(guest_list)

print(f'Dear {guest_selected}, you have won {prize_selected} as a prize. ')

for guest in guest_list:
