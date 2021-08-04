from random import randint

# Создание исходного массива

list_a = []
for i in range(100):
    list_a.append(randint(-50, 50))
print(list_a)

# Создание массива из отрицательных чисел исходного
list_b = []

for elem in list_a:
    if elem < 0:
        list_b.append(elem)
print(list_b)
# поиск максимального отрицательного значения и определения его места в первом массиве

min_num = max(list_b)
min_index = 0

for elem in list_a:
    if elem == min_num:
        min_index = list_a.index(elem)

print(f'Максимальное минимальное значение {min_num} на позиции {min_index + 1}')
