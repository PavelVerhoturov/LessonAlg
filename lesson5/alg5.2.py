from collections import defaultdict
from collections import deque

symbol_hex = '0123456789ABCDEF'
value = defaultdict(int)
count = 0
for i in symbol_hex:
    value[i] += count
    count += 1


def user_dex(facts):
    dex = 0
    num = deque(facts)
    num.reverse()
    for i in range(len(num)):
        dex += value[num[i]] * 16 ** i
    return dex


def user_hex(number):
    numb = deque()
    while number > 0:
        dex = number % 16
        for j in value:
            if value[j] == dex:
                numb.append(j)
        number //= 16
    numb.reverse()
    return list(numb)


a = input(f'Введите число в шестнадцатеричном формате - ')
a = a.upper()
b = input(f'Введите второе число в шестнадцатеричном формате - ')
b = b.upper()
dex_a = user_dex(a)
dex_b = user_dex(b)
# print(dex_a, dex_b)
print(f'{a} + {b} = {user_hex(dex_a + dex_b)}')
print(f'{a} * {b} = {user_hex(dex_a * dex_b)}')
