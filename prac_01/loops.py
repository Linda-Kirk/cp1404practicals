def main():

    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 101, 10):
        print(i, end=' ')
    print()

    for i in reversed(range(1, 21, 1)):     # One way to reverse range
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):              # Another way to reverse range
        print(i, end=' ')
    print()

    number_stars = int(input('Enter number of stars: '))
    for i in range(number_stars):
        print('*', end=' ')
    print()

    for i in range(number_stars + 1):
        print('*' * i)
    print()

    # Lindsay's solution below:
    for i in range(number_stars + 1):
        print('* ' * i)
    print()


main()
