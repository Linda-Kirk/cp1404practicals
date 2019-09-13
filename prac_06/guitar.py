"""CP1404 Practical - Guitar class."""

from datetime import date


class Guitar:
    VINTAGE_THRESHOLD = 50

    def __init__(self, make='', model=',', year=0, cost=0.0):
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{self.make} {self.model} ({self.year}) : ${self.cost:,.2f}'.format(self=self)

    def get_age(self):
        today = date.today()
        return today.year - self.year


def run_tests():
    # first_guitar = Guitar((input('Guitar: ')))
    make = "Gibson"
    model = "L-5 CES"
    year = 1922
    cost = 16035.40
    first_guitar = Guitar(make, model, year, cost)

    print(first_guitar)
    print(first_guitar.get_age())
    print(first_guitar, "Age: {}".format(first_guitar.get_age()))


if __name__ == '__main__':
    run_tests()
