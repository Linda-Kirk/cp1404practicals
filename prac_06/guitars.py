"""CP1404 Practical - Client code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print('My Guitars!')
    # make = input('Make: ')
    # while make != '':
    #     model = input('Model: ')
    #     year = int(input('Year: '))
    #     cost = float(input('Cost: '))
    #     guitar_details = Guitar(make, model, year, cost)
    #     guitars.append(guitar_details)
    #     make = input('Make: ')

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars):
        vintage_string = ' (Vintage)' if guitar.is_vintage() else ''
        print("Guitar {}: {:20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.make, guitar.model, guitar.year,
                                                                 guitar.cost, vintage_string))


main()
