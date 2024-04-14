import requests

from openpyxl import Workbook

# make request to API to get list of countries
countries_url = 'https://country-list-1150.azurewebsites.net/api/country'

# naming variables correctly is very important
countries_list_response = requests.get(countries_url).json()
# printing the list of countries
print(countries_list_response)

# creating a workbook
country_workbook = Workbook()
country_worksheet = country_workbook.active
country_worksheet.title = 'Countries and Capital Cities'

# we put row to be 0 so it starts from the first row on the spreadsheet
row = 0

# get individual country and capital
for individual_country_dictionary in countries_list_response:
    country_name = individual_country_dictionary['name']
    print(country_name)
    # row +1 will increment row by 1
    row = row + 1
    country_worksheet.cell(1, 1, country_name)

# we are going to save the workbook
country_workbook.save('countries_and_capitals.xlsx')



