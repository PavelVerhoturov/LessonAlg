a = int(input('Введите последовательность '))
b = int(input('Введите цифру для поиска '))
i = 0
while a != 0:
    n = a % 10
    a //= 10
    if n == b:
        i += 1
print(i)