"""Client code to test Taxi class"""

from prac_08.taxi import Taxi


def main():
    name = "Prius 1"
    fuel = 100
    price_per_km = 1.23
    taxi_1 = Taxi(name, fuel, price_per_km)
    print(taxi_1)

    taxi_1.drive(40)
    print("{}, current fare=${:.2f}".format(taxi_1, taxi_1.get_fare()))

    taxi_1.start_fare()
    taxi_1.drive(100)
    print("{}, current fare=${:.2f}".format(taxi_1, taxi_1.get_fare()))


main()
