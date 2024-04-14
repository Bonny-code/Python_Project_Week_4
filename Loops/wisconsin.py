# here we want the user to make many attempts in getting the answer right and when he does the loop will end.

# We start by prining out the quiz and asking the user a question for the capital of wisconsin.
print('Quiz Program')

# we save the answer in a variable called answer
answer = input('What is the Capital of Wisconsin? ')

# a while loop is used to ask until the user eventually gets it right.
# if the answer is not madison, it will print the quote in the print statement and then ask again
# this will continue until the user gets the correct answer which will then print correct as can
# be seen in the else statement
while answer.lower() != 'madison':
    print('Sorry, that is not right. Please try again ')
    answer = input('What is the capital of wisconsin ')
else:
    print('correct')
