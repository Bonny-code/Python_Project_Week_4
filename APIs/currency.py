import requests

# always start by importing requests
# save the api in a variable like below
url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD&symbols=EUR'

# using an input statement to ask number of dollars
dollars = float(input('Enter number of Dollars: '))

# to get get the values from the api
response = requests.get(url).json()

# printing a specific value or rates
rates = response['rates']
print(rates)

# searching and printing a pecific value for EUR
exchange_rates = rates['EUR']
print(exchange_rates)

# calculating the dollar conversion rate to euros and printing
euros = dollars * exchange_rates
print(f'${dollars} is equivalent to {euros:.2f} euros.')