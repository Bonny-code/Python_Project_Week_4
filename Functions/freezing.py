# we will call the temperature funtion in different ways
#

def above_freezing(temp):
    if temp > 32:
        return 'Above freezing'
    else:
        return 'Below freezing'


def main():
    today_temp = float(input('Please enter today \'s high temperature: '))
    # calling the function in a print statement
    print('it wil be ' + above_freezing(today_temp) + 'today')

    tonight_temp = float(input('Please enter today \'s low temperature: '))
    # we are calling the function and saving the return in a variable
    # and using it later in the print statement
    above_below_tonight = above_freezing(tonight_temp)
    print('It will be ' + above_below_tonight + ' tonight')

    tomorrow_temp = float(input('Please enter tomorrow \'s low temperature: '))
    # calling the function in an f string
    print(f'it will be {above_freezing(tomorrow_temp)}')


main()
