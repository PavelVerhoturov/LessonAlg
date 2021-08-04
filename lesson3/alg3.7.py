from random import randint

# Создание исходного массива

list_a = []
for i in range(100):
    list_a.append(randint(0, 99))
print(list_a)

list_a.sort()
print(f'Самые наименьшие два числа {list_a[0]} и {list_a[1]}')

# Вроде все правильно, но чувство обмана не покидает
