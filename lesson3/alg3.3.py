from random import randint
# Создание  массива

list_a = []
for i in range(10):
    list_a.append(randint(0, 100))
print(list_a)
# Поиск мин и макс числа, а также их индексов

max_num = list_a[0]
min_num = list_a[0]

for i in list_a:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(f'Максимальное число {max_num}')
print(f'Минимальное число {min_num}')
max_index = list_a.index(max_num)
min_index = list_a.index(min_num)


# Перестановка числел
list_a[max_index], list_a[min_index] = list_a[min_index], list_a[max_index]
print(list_a)

