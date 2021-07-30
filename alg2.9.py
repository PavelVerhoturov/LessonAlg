num = input("Введите числа через пробел ").split()
max_sum = 0
max_num = 0
value = 0
elem = 0
for i in num:
    elem = i
    digit = 0
    for value in elem:
        digit += int(value)
    if max_sum < digit:
        max_sum = digit
        max_num = int(elem)

print(f'Число {max_num}, сумма {max_sum}')
