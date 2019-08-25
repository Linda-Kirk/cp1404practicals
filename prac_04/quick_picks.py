"""
This program will generate "quick picks". The number of quick picks required
will be obtained from user. The program will then generate that many lines of
output. Each line will consist of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
"""

import random

QUANTITY_NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_quick_picks = int(input('Enter the number of quick picks required: '))

for quick_pick in range(number_quick_picks):
    numbers = []
    while len(numbers) < QUANTITY_NUMBERS_PER_LINE:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print('{:2}'.format(numbers))
