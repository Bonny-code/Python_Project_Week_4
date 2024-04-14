# How many books does the user need

number_of_books = int(input('how many books to buy '))

# create a vairable for the total set to 0
total = 0

# here we are repeating the loop once per book
for book in range(number_of_books):
    book_price = float(input('Enter book price $'))
    # if the price is return as 0 then the book is free
    if book_price == 0:
        print('Yay the book if free')
    # here we will add the book price to the total
    total = total + book_price
print(f'The total price for all {number_of_books} is ${total}')

