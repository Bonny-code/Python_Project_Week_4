# will return true if the password is true and false
#  if the password is not
# notice that the function is always called at the end of the code.

def is_password_long_enough(password):
    if len(password) >= 8:
        return True
    else:
        return False


def main():

    password = 'kittens'
    if is_password_long_enough(password):
        print(f'The password {password} is long enough. ')
    else:
        print(f'The password {password} is NOT long enough. ')


main()

