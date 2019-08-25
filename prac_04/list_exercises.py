def main():
    numbers = []
    for user_entry in range(5):
        number = int(input('Number: '))
        numbers.append(number)

    print('The first number is {}'.format(numbers[0]))
    print('The last number is {}'.format(numbers[-1]))
    print('The smallest number is {}'.format(min(numbers)))
    print('The largest number is {}'.format(max(numbers)))
    print('The average of the numbers is {}'.format((sum(numbers) / len(numbers))))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_name = input('Enter User Name: ')
    if user_name in usernames:
        print('Access granted')
    else:
        print('Access denied')


main()
