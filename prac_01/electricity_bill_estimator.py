"""
This program is estimates an electricity bill
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print('Electricity bill estimator 2.0')
    tariff = input('Which tariff? 11 or 31: ')
    while tariff not in ('11', '31'):
        print('Invalid tariff!')
        tariff = int(input('Which tariff? 11 or 31: '))

    if tariff == '11':
        tariff = TARIFF_11
    else:
        tariff = TARIFF_31

    daily_use_kwh = float(input('Enter daily use in kWh: '))
    number_billing_days = int(input('Enter number of billing days: '))

    estimated_bill = daily_use_kwh * number_billing_days * tariff
    print('Estimated bill: ${:,.2f}'.format(estimated_bill))


main()
