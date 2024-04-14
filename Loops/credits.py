number_of_credits = int(input('how many credits are you taking this semester '))

# here this loop will keep repeating as long as the answer is negative
while number_of_credits < 0:
    print('Error - Please enter 0 or a positive number')
    number_of_credits = int(input('Enter the number of credits you are taking this semester '))

if number_of_credits >= 12:
    print('You are a full time student')
elif number_of_credits >= 6:
    print(' You are a half time student')
else:
    print('You are less than half')