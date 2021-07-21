a = 0
b = 0
num = int(input('Введите натуральное число '))
while num // 10 != 0:
    c = num % 10
    if c % 2 == 0:
        a += 1
    else:
        b += 1
    num //= 10
if num % 2 == 0:
    a += 1
else:
    b += 1
print(f'Четныйх цифр - {a}, нечетный - {b}')
