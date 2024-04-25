import requests

# as usual, we import requests and save the api in a url like below
url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD&symbols=EUR'

# we use the response to get the api
response = requests.get(url).json()
print(response)

rates = response['rates']
print(rates)

#  asking the user to enter an mount they want to convert
# we also use float
dollars = float(input('Enter number of Dollars: '))
print('Here are the correct currency cods ')
list_of_codes = list(rates.keys())

#  we are using .sort to sort the values of the different currencies.
list_of_codes.sort()
print(', '.join(list_of_codes))

currency_code = input('Enter the currency code to convert to. ')

# This will show the rates in the currency you typed above
# we use an if or else statement to determine what happens if the user inputs an
# incorrect value as it will print not a valid currency code.
exchange_rates = rates[currency_code]
if exchange_rates is None:
    print('Not a valid currency code')
else:
    converted_value = dollars * exchange_rates
    print(f'${dollars} is equivalent to {converted_value:.2f} {currency_code}.')
