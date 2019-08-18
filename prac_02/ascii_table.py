"""
This program will generate an ASCII code when a character is inputted by a user
or generate a character when an ASCII code inputted by a user
"""
LOWER = 33
UPPER = 127


character = input("Enter a character: ")

print("The ASCII code for {} is {}".format(character, ord(character)))

ascii_code = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while not LOWER <= ascii_code <= UPPER:
    print("Invalid Number")
    ascii_code = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(ascii_code, chr(ascii_code)))

# ASCII Two Column Table
for value in range(LOWER, UPPER + 1):
    print("{:3} {:>3}".format(value, chr(value)))


