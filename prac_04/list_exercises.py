def main():
    numbers = []
    for user_entry in range(5):
        number = input('Number: ')
        numbers.append(number)

    print('The first number is {}'.format(numbers[0]))
    print('The last number is {}'.format(numbers[-1]))
    print('The smallest number is {}'.format(min(numbers)))
    print('The largest number is {}'.format(max(numbers)))



main()
