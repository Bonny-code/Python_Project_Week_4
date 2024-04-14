
# we want to limit the number of attempts the user has to get the right answer to 3.

print('Quiz Program')

# we start by asking a question and saving the answer into a variable called answer
answer = input('What is the Capital of Wisconsin? ')

#  the count parameter is used since we will limit the number of attempts the user has.
count = 1

# a while loop is used to determine what to do if the answer is not madison
while answer.lower() != 'madison':
    print('Sorry, that is not right. Please try again ')
    count = count + 1
    # we increment the count parameter by 1 each time the user attempts the question
    answer = input('What is the capital of wisconsin ')
    if count == 3:
        # if the user makes more than 3 attempts incorrectly, that will be the end of the quiz
        print('Sorry you have used all your chances.')
        # then break word below is used to break out of the loop if not it will keep repeating
        break
# but if the ser gets it right the first time, then it will print the message below.
else:
    print('correct! you got the answer in one guess(es)')



