import requests
# we import requests and save the api in a api
url = 'https://api.weather.gov/gridpoints/MPX/107,71/forcast'

response = requests.get(url).json()
# print(response)

# this is to get specific things from the api
properties = response['properties']
# print(properties)
forcast_periods = properties['periods']
# print(forcast_periods)

# we use a for loop to get the values of name temp and the forcast
# the spellings have to match that of the api
# we print all of them
# the <17 is used to make them appear in a tabular manner.
for period in forcast_periods:
    name = period['name']
    temp = period['temperature']
    forecast = period['detailedForcast']
    print(f'{name:<17}, {temp:<17}F, {forecast}')