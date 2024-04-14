# Here we are writing a function to print out a name in capital letters.
# we start by creating the first function with a message of hello the username
# the first function is the greetings function which will return the name variable
# the second function has a username defined, and it will call the greetings function
# we will use the .upper to convert the letter to uppercase's.
# we will now print the new name and call the main function at the end.
def greetings(name):
    message = f'Hello {name}'
    return message


def main():
    username = input('What is your name? ')
    hello_message = greetings(username)
    new_name = hello_message.upper()
    print(new_name)


main()
