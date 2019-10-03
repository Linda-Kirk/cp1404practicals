"""Client code to test SilverServiceTaxi class"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)

    hummer.drive(25)
    print("{}, current fare=${:.2f}".format(hummer, hummer.get_fare()))

    hummer.start_fare()
    hummer.drive(5)
    print("{}, current fare=${:.2f}".format(hummer, hummer.get_fare()))

    mercedes = SilverServiceTaxi("Mercedes", 75, 2)

    mercedes.drive(18)
    print("{}, current fare=${:.2f}".format(mercedes, mercedes.get_fare()))


main()
