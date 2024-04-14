def first_year_second_year(class_code):
    # if class code is between 1000 - 1999 it will return first year
    if 1000 <= class_code <= 1999:
        return 'First year'
    # the code is rewritten shorter
    elif 2000 <= class_code <= 2999:
        return 'Second year'
    else:
        return 'Invalid code'

# the main function will always run first before your logic function
# always run the logic in your defined function
# and then the main function runs the questions.

def main():
    code = int(input('Please enter your class code: '))
    result = first_year_second_year(code)
    print(result)


main()
