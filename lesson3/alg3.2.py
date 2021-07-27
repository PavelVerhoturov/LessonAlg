from random import randint
# Создание первого массива

array_num = []
for i in range(10):
    array_num.append(randint(0, 100))
    
print(f'Массив - {array_num}')
# Четные индексы первого масива

even_index = []
for i in array_num:
    if i % 2 == 0:
        even_index.append(array_num.index(i))

print(f'Четные индексы массива  - {even_index}')




