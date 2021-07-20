from random import randint, uniform


type = input('Введите тип - int, float или str ')
a = input('Введите начало диапазона ')
b = input('Введите конец диапазона ')

if type == 'int':
    result = randint(int(a), int(b))
    print(f'Случайное целое число из диапазона {a} и {b} = {result}')
elif type == 'float':
    result = uniform(float(a), float(b))
    print(f'Случайное вещественное число из диапазона {a} и {b} = {result}')
elif type == "str":
    result = chr(randint(ord(a), ord(b)))
    print(f'Случайный символ из диапазона {a} и {b} = {result}')
else:
    print('Введен не коректный тип диапазона')
