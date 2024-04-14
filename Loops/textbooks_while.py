
total = 0

more_books = True

while more_books:
    book_price = float(input(' Enter the price of a textbook'))
    total = total + book_price
    any_more = input('Any more books  Type "Y" for yes or "N" for no: ')
    if any_more == 'N':  # to accept lowercase n, u will have to use n.upper
        more_books = False
print(f'The total of all books is {total}')