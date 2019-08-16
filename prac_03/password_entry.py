"""
Linda Kirk
Program will ask user for a password, with error-checking to repeat if the password doesn't meet a
minimum length set by a variable.
Will print asterisks as long as the password.
Example: if the user enters "Pythonista" (10 characters), the program should print "**********".
"""
MINIMUM_LENGTH = 10


def main():
    password = get_password()
    print_astrix_password(password)


def print_astrix_password(password):
    print('*' * len(password))


def get_password():
    password = input('Enter a password (must be at least {} characters in length): '.format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print('Password is too short!')
        password = input('Enter a password (must be at least {} characters in length): '.format(MINIMUM_LENGTH))
    return password


main()
