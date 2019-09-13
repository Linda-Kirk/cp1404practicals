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


def run_tests():
    first_guitar = Guitar((input('Guitar: ')))
    print(first_guitar)


if __name__ == '__main__':
    run_tests()
