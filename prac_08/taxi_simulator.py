"""CP1404 Practical - taxi simulator to use the Taxi and SilverServiceTaxi class."""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
PROMPT = ">>>"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Mercedes", 75, 1.5), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    bill_to_date = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_choice = input(PROMPT).upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            current_taxi = get_taxi_choice(taxis)
        elif menu_choice == 'D':
            if current_taxi is not None:
                bill_to_date += drive_taxi(current_taxi)
            else:
                print("A taxi must be chosen before it can be driven")
        else:
            print("Invalid menu choice")
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        menu_choice = input(PROMPT).upper()

    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi):
    current_taxi.start_fare()
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
    return trip_cost


def get_taxi_choice(taxis):
    taxi_choice = 0
    print("Taxis available:")
    display_taxis(taxis)

    valid_taxi_number = False
    while not valid_taxi_number:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0:
                print("Number must be >= 0")
            elif taxi_choice > len(taxis) - 1:
                print("Invalid taxi choice number")
            else:
                valid_taxi_number = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return taxis[taxi_choice]


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
