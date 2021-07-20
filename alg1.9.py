a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if a > b and b > c or c > b and b > a:
    print(f'Среднее число из списка {b}')
else:
    if b > a and a > c or c > a and a > b:
        print(f'Среднее число из списка {a}')
    else:
        print(f'Среднее число из списка {c}')
