# our function is going to take a quiz question and answer
# we start by creating a function called quiz which will print out the various questions
# the prompt will ask the user for a response after displaying the questions.
# we will use an if and else statement to determine if the answer is correct.
# if the answer is correct, we will print that the user got it right
# if the answer is incorrect, we will print the right answer for the user.
# we are adding the .lower to convert everything into lower cases incase the user types in
# the answer in different cases.
# The Main function is where we are defining the questions and the answers
# after which we call the function at the end.


def quiz(quiz_question, correct_answer):
    print(quiz_question)
    user_response = input('Please enter your answer: ')
    if user_response == correct_answer:
        print('You got the right answer')
    else:
        print(f'the right answer is {correct_answer}')


def main():
    question1 = 'Which planet is closest to the sun? '
    answer1 = 'Mecury'
    answer1.lower()

    question2 = 'Who painted the Mona Lisa? '
    answer2 = 'Leonardo da Vinci'
    answer2.lower()

    quiz(question1, answer1)
    quiz(question2, answer2)


main()
