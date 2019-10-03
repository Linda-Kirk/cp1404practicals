"""CP1404 Practical - taxi simulator to use the Taxi and SilverServiceTaxi class."""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Mercedes", 75, 1.5), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    bill_to_date = 0
    current_taxi = None
    # TODO: Find out how this is supposed to work!

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input('>>>').upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == 'D':
            try:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                bill_to_date += trip_cost
            except AttributeError:
                print("A taxi must be chosen before it can be driven")
        else:
            print('Invalid menu choice')
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input('>>>').upper()

    print("Total tip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
