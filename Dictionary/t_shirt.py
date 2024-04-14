# A list of the days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# an empty list to hold the values of the sales the user will type in
sales = {}

# a for loop to input the amount of sales for each day of the week
for day in days_of_week:
    tshirt_sold = int(input(f'How many t-shirt sold in {day}  '))
    sales[day] = tshirt_sold

# we are printing all the sales data the user entered
# the first print is to create a space
print()
print('Here is all the sales data you entered: ')

# here we are printing both the days of the week and the amount of t-shirt sold
for day, tshirt_sold in sales.items():
    print(f'on {day} there was {tshirt_sold} t-shirt sold. ')

# calculating total amount of sales for the week
total_sales = sum(sales.values())

# Average sales per month - the total, divided by the number of days
months = len(sales)
average = total_sales / months

# to put an up arrow
up_arrow = chr(8593)

# to put a down arrow
down_arrow = chr(8595)

# printing the up and down arrows if sales are up or down
# using an if statement
if months >= average:
    print(up_arrow)
else:
    print(down_arrow)

# here we are printing all the data
print()
print(f'The total amount of sales in {months} days is {total_sales} . ')
print(f'The average amount of sales per week is {average:.2f} ')