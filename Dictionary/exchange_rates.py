rates = {
    'AUD': 1.5311,
    'BGN': 1.9558,
    'BRL': 4.9682,
    'CAD': 1.3351,
    'CHF': 0.9863,
    'CNY': 7.0894,
    'CZK': 24.422,
    'DKK': 7.4419,
    'EUR': 1,
    'GBP': 0.87478,
    'HKD': 7.7493,
    'HRK': 7.5353,
    'HUF': 401.15,
    'IDR': 15491.81,
    'ILS': 3.5065,
    'INR': 81.02,
    'ISK': 145.5,
    'JPY': 145.19,
    'KRW': 1397.7,
    'MXN': 19.2611,
    'MYR': 4.6872,
    'NOK': 10.2019,
    'NZD': 1.6769,
    'PHP': 57.672,
    'PLN': 4.6825,
    'RON': 4.8893,
    'RUB': 86.7666,
    'SEK': 10.8538,
    'SGD': 1.3891,
    'THB': 36.906,
    'TRY': 18.3845,
    'USD': 0.9872,
    'ZAR': 17.7983
}

# i am using a variable to stor what the user will type in
conversion = str(input('What currency code would you like to convert to? '))

# the amount refers to how much the user wants to convert
amount = int(input('how many Euros would you like to convert? '))

# we are using the in word to compare if the currency te ser types in is amongst the rates
# we have available in the list
# it will also print out the value of the currency the user types in
if conversion in rates:

    # we are saving the number in a variable below
    print(f'here\'s you exchange rate {rates[conversion]}')
else:
    # what will pop up if the currency is not on the list
    print('The currency you entered is not on the list and the conversion cannot be done')

# we are saving the conversion rate in a variable
user_input_value = rates[conversion]

# converting the currency amount the user types in
convert_currency = amount * user_input_value

# printing the value of the converted currency
print(f'the converted amount is {convert_currency} in {conversion}')
