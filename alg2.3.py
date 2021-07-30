num = int(input('Введите число '))
b = num
num_rev = 0
while num != 0:
    num_rev = num_rev * 10 + num % 10
    num //= 10

print(f'реверс числа {b} {num_rev}')
