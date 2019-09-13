"""CP1404 Practical - Client code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print('My Guitars!')
    make = input('Make: ')
    while make != '':
        model = input('Model: ')
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        guitar_details = Guitar(make, model, year, cost)
        print(guitar_details)
        make = input('Make: ')

    print(guitar_details)


# print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))


main()
