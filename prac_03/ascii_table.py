"""
This program will generate an ASCII code when a character is inputted by a user
or generate a character when an ASCII code inputted by a user
"""
LOWER = 10
UPPER = 50


def main():
    character_valid = False
    while not character_valid:
        character = input("Enter a character: ")
        if len(character) > 1:
            print("Only enter one (1) character")
        else:
            character_valid = True

    print("The ASCII code for {} is {}".format(character, ord(character)))

    ascii_code = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(ascii_code, chr(ascii_code)))

    # ASCII Two Column Table
    # for value in range(LOWER, UPPER + 1):
    #     print("{:3} {:>3}".format(value, chr(value)))


def get_number(lower, upper):
    valid_number = False
    while not valid_number:
        try:
            number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            if not lower <= number <= upper:
                print("Please enter a valid number!")
            else:
                valid_number = True
        except ValueError:
            print("Please enter a numeric number")
    return number


main()
