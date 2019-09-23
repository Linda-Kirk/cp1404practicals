"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car

initial_fuel_quantity = 100

print("Let's drive!")
car_1 = Car(input("Enter your car name: "), initial_fuel_quantity)
distance = (int(input("How many km do you wish to drive? ")))
drive_distance = car_1.drive(distance)
if distance <= drive_distance:
    print("The car drove {}km.".format(drive_distance))
else:
    print("The car drove {}km and ran out of fuel.".format(drive_distance))
print(car_1)
