# This code is to determine if a user's Windows computer can be upgraded
# For that to happen, the user has to fulfill certain conditions
# Here we start by creating the main function which often runs first
# and that is where most of the questions will be asked.
# we ask the user for how much free memory they have which will be an integer
# same thing for storage space
# finally the operating system on the computer.
def main():
    print('Can your computer be upgraded to windows 11? ')
    free_memory = int(input('What is your computer memory? '))
    free_storage = int(input('What is your free storage space?  '))
    operating_system = input('What is the name of your computers operating system? ')

    windows_11_compatible(free_memory, free_storage, operating_system)

    # here we called the windows_11_compatible function which is below and passing all the
    # variables inside

    # below, we want to print something if the statement is true or false
    # so the code below serves that purpose.
    # This is also because we have to define what true or false is by
    # attaching a print statement to them.
    if windows_11_compatible:
        print('Congratulations, your computer can be upgraded')
    else:
        print('Unfortunately, your computer cannot be upgraded')


# below is the windows_11_compatible function which
# runs the logic of the application
# if all the statements are correct then the program will return True
# which wil then show the print message above when it is true
# and the same thing happens if the program returns false.
# the logic is that the memory has to be 8 or above, storage has to be
# 64 or above and operating system has to be Windows 10.
# if all these conditions are met then the user's computer can be upgraded else it cannot.


def windows_11_compatible(free_memory, free_storage, operating_system):
    if free_memory >= 8 and free_storage >= 64 and operating_system == 'Windows 10':
        return True
    else:
        return False


main()
