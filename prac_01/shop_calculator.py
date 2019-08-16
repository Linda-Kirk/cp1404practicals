"""
Programme to calculate 10% discount on one or more products
valued greater than $100. Discounted price is displayed
"""


def main():
    total_cost = 0
    discount_rate = .10

    number_of_items = int(input('Number of items: '))
    while number_of_items < 0:
        print('Invalid number of items!')
        number_of_items = int(input('Number of items: '))

    for i in range(number_of_items):
        price = float(input('Price of item: '))
        total_cost += price

    if total_cost > 100:
        discount_amount = total_cost * discount_rate
        total_cost -= discount_amount

    print('Total price for {} items is ${:,.2f}'.format(number_of_items, total_cost))


main()
