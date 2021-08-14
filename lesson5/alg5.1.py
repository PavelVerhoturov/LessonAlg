from collections import namedtuple

company = namedtuple('New_comp', [
    'name',
    'first',
    'second',
    'third',
    'fourth'
])
income_dict = {}
sum_income = 0
num = int(input('Введите колличество компаний - '))
for i in range(num):
    company.name = input('Введите имя компании - ')
    company.first = float(input('Введите прибыль за первый квартал - '))
    company.second = float(input('Введите прибыль за второй квартал - '))
    company.third = float(input('Введите прибыль за третий квартал - '))
    company.fourth = float(input('Введите прибыль за четвертый квартал - '))
    income = company.first + company.second + company.third + company.fourth
    income_dict.update({company.name: income})
    sum_income += income

comp_avg = sum_income / num
for name, comp_income in income_dict.items():
    if comp_income > comp_avg:
        print(f'Прибыль {name} составила {comp_income}, она меньше {comp_avg}')
for name, comp_income in income_dict.items():
    if comp_income < comp_avg:
        print(f'Прибыль {name} составила {comp_income}, она больше {comp_avg}')
