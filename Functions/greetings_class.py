# this is the greetings function
# we start by creating the first function with a message of hello the uersname
# the first function is the greetings function which will return the name variable
# the second function has a username defined and it will call the greetings function
# we will use the .upper to convert the letter to uppercase's.
# we will now print the new name and call the main function at the end.
# the order in which u call your function does not really matter but main has to be at the bottom
# since it is the function that runs first.

def greeting(name):
    message = f'Hello {name}!'
    return message


def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)


main()