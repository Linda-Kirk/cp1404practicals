"""Client code to test UnreliableCar class"""

from prac_08.unreliable_car import UnreliableCar


def main():
    name = "The Bomb"
    fuel = 100
    reliability = 20
    unreliable_1 = UnreliableCar(name, fuel, reliability)
    print(unreliable_1)

    unreliable_2 = UnreliableCar("Trusty", 100, 90)
    print(unreliable_2)

    print("Initial Test Drive")
    print("{} drove {}km".format(unreliable_1.name, unreliable_1.drive(20)))
    print(unreliable_1)
    print("{} drove {}km".format(unreliable_2.name, unreliable_2.drive(20)))
    print(unreliable_2)

    print("Multiple Drive Test")
    for index in range(1, 10):
        print("{} drove {}km".format(unreliable_1.name, unreliable_1.drive(index)))
        print("{} drove {}km".format(unreliable_2.name, unreliable_2.drive(index)))

    print(unreliable_2)
    print(unreliable_1)


main()
