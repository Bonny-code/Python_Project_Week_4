# list of months
months = ['June', 'July', 'August']

# rainfall is an empty dictionary
rainfall_per_month = {}

# loop over month list
for month in months:
    rain = float(input(f'How much snow in {month},'))
    rainfall_per_month[month] = rain

print(rainfall_per_month)

#  printing all the data
# always add .items to get keys and values
for month, rain in rainfall_per_month.items():
    print(f'In {month} its rained {rain} inches')

# total rain
total = sum(rainfall_per_month)

#  average
# the len function gives the number of key value pairs
number_of_months = len(rainfall_per_month)
average = total / number_of_months

# printing everything
print(f'The average for {number_of_months} months is {average} inches. ')