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
while number_quick_picks <= 0:
    print('Need a minimum of 1 quick pick')
    number_quick_picks = int(input('Enter the number of quick picks required: '))

for quick_pick in range(number_quick_picks):
    numbers = []
    while len(numbers) < QUANTITY_NUMBERS_PER_LINE:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()

    for number in numbers:
        print('{:2}'.format(number), end=' ')
    print()

# Lindsay's solution below - need to ask how this works
#     print(' '.join('{:2}'.format(number) for number in numbers))
