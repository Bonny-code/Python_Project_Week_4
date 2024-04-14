# this function is to convert the number of miles to kilometers
# we start with the main function which often runs first
# to get the km, we multiply miles by 1,60934


def main():
    miles = float(input('Please enter a number of miles'))
    kilometers = miles_to_kilometers(miles)
    print(f'{miles} miles is equal to {kilometers}')


def miles_to_kilometers(miles):
    km = miles * 1.60934
    return km


main()