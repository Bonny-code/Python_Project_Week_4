# a list of the number of months with snowfall
winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April']

# an empty dictionary to hold what the user types in.
snowfall = {}

# we are using for loop to ask the user to input how much snow for each month
# this will appear for every month of the winter months in the dict above
for month in winter_months:
    snow = float(input(f'How much snow in {month}, in inches '))
    snowfall[month] = snow

# print and empty line the present the data entered below
print()
print('Here is all of the data you entered: ')

# here we are printing both the month and snow which represents
# the key and value
# to print both, u have to use the .items keyword
for month, snow in snowfall.items():
    print(f'in {month} there was {snow} inches of snow. ')

# calculating total amount of snow
total_snow = sum(snowfall.values())

# Average snowfall per month - the total, divided by the number of months
months = len(snowfall)
average = total_snow / months

# printing everything to display the last information
print()
print(f'The total amount of snow in {months} months is {total_snow} inches. ')
print(f'The average amount of snow per month is {average:.2f} inches ')
