# we always hae to import request and download it to use it
import requests

# use a variable to save the API URL which you can call at anytime.
url_north = 'http://svc.metrotransit.org/NexTrip/17940?format=json'

url_south = 'http://svc.metrotransit.org/NexTrip/17928?format=json'

# we use a variable to save the contents of the api if we call it
# we also use the request key word and the get keyword to get the url and save
# it in a json format
north_response = requests.get(url_north).json()

# we print the contents of the url
print(north_response)

# same thing with the south api
south_response = requests.get(url_south).json()
print(south_response)

# we are focusing more on some key data from the north link
# we want only the departure times
north_departures = north_response['departures']
print(north_departures)


# here we are writing a for loop to get certain data from the api

for bus_info in north_departures:
    print(bus_info)
    description = bus_info['description']
    departure_text = bus_info['departure_text']
    route_id = bus_info['route_id']
    # we are trying to print the data in a column format
    # the f string is used to print data and can be adjusted in this format
    # this is a good way to print data in a column or table
    print(f'Route-Description                Time                 Route ')
    print(f'{description:<20}        {departure_text:<20}{route_id:<20}')


