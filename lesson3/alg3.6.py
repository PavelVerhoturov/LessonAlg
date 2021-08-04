from random import randint

# Создание исходного массива

list_a = []
for i in range(10):
    list_a.append(randint(0, 99))
print(list_a)
# Определяем максимальное и минимальное занчение, а так же их индексы

max_num = max(list_a)
min_num = min(list_a)
max_index = list_a.index(max_num)
min_index = list_a.index(min_num)

# Так как индекс максимально числа может быть маньше минимального определяем так же шаг

if max_index - min_index > 0:
    step = 1
else:
    step = -1

# Ищем сумму
sum_elem = 0
for elem in list_a[min_index + step:max_index:step]:  # честно идею стащил с гугла не разобравшись
    sum_elem += elem
print(f'Сумма минимальным и максимальным элементом = {sum_elem}')
