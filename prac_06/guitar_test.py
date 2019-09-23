"""CP1404 Practical - Client code to use and test the Guitar class."""

from prac_06.guitar import Guitar


def main():
    make = "Gibson"
    model = "L-5 CES"
    year = 1922
    cost = 16035.40
    first_guitar = Guitar(make, model, year, cost)

    make = "Gibson"
    model = "LES PAUL SG"
    year = 2012
    cost = 6399.00
    another_guitar = Guitar(make, model, year, cost)

    # print(first_guitar)
    # print(first_guitar.get_age())
    # print(first_guitar.is_vintage())
    # print(first_guitar, ". Age: {}, Vintage: {}".format(first_guitar.get_age(), first_guitar.is_vintage()))

    print(first_guitar, ". Age: {}, Vintage: {}".format(first_guitar.get_age(), first_guitar.is_vintage()))
    print(another_guitar,
          ". Age: {}, Vintage: {}".format(another_guitar.get_age(), another_guitar.is_vintage()))
    print('{} {} get_age() - expected 97, Got {}'.format(first_guitar.make, first_guitar.model, first_guitar.get_age()))
    print('{} {} get_age() - expected 7, Got {}'.format(another_guitar.make, another_guitar.model,
                                                        another_guitar.get_age()))
    print('{} {} is_vintage() - expected True, Got {}'.format(first_guitar.make, first_guitar.model,
                                                              first_guitar.is_vintage()))
    print('{} {} is_vintage() - expected False, Got {}'.format(another_guitar.make, another_guitar.model,
                                                               another_guitar.is_vintage()))


main()
