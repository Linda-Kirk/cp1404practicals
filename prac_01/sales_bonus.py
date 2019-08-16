"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_RATE_1 = .10
BONUS_RATE_2 = .15


def main():

    sales = float(input('Enter total sales: $'))
    while sales >= 0:
        if sales < 1000:
            bonus_rate = BONUS_RATE_1
        else:
            bonus_rate = BONUS_RATE_2
        bonus = sales * bonus_rate
        print('Total Sales: ${:>13,.2f}'.format(sales))
        print('Bonus Rate: {:.2%}'.format(bonus_rate))
        print('Total Bonus: ${:>13,.2f}'.format(bonus))
        sales = float(input('Enter total sales (-ve to quit): $'))


main()
