from random import randint

# Создание  массива

list_a = []
for i in range(100):
    list_a.append(randint(0, 50))
print(list_a)

repeat_num = 0  # число с максимальным колличеством повторов
for i in list_a:
    if list_a.count(repeat_num) < list_a.count(i):
        repeat_num = list_a.index(i)

print(f'Число {repeat_num} встречается {list_a.count(repeat_num)} раз(а)')

