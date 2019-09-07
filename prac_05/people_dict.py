from datetime import date

people_dict = {}

for person in range(3):
    name = input('Name: ')
    date_of_birth_list = input('Date of Birth (DD/MM/YYYY): ').split('/')
    date_of_birth_list = [int(number) for number in date_of_birth_list]
    people_dict[name] = date_of_birth_list

length_longest_name = max([len(name) for name in people_dict.keys()])
for name, day_month_year in people_dict.items():
    today = date.today()
    age = today.year - day_month_year[2] - (
            (today.month, today.day) < (day_month_year[1], day_month_year[0]))
    print('{:{}}: {}'.format(name, length_longest_name, age))
