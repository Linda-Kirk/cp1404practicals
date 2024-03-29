"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When anything other than an integer is entered
2. When will a ZeroDivisionError occur? When a 0 is entered as denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Add a while
    loop when entering denominator?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

