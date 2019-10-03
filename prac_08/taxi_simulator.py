"""CP1404 Practical - taxi simulator to use the Taxi and SilverServiceTaxi class."""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Mercedes", 75, 1), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input('>>>').upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))

        elif menu_choice == 'D':
            print(menu_choice)
        else:
            print('Invalid menu choice')
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input('>>>').upper()


main()
