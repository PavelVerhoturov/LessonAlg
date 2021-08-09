# 3 урок 4 задача
# Определить, какое число в массиве встречается чаще всего.
# Решение
import time
import timeit
from random import randint


def task3_4():
    list_a = []
    for i in range(100):
        list_a.append(randint(0, 50))
    print(list_a)

    repeat_num = 0  # число с максимальным колличеством повторов
    for i in list_a:
        counter = list_a.count(repeat_num)
        if counter < list_a.count(i):
            repeat_num = list_a.index(i)

    print(f'Число {repeat_num} встречается {counter} раз(а)')


def task3_4_v2():
    list_a = []
    for i in range(100):
        list_a.append(randint(0, 50))
    print(list_a)

    result = list_a[1]
    max_counter = 0
    for i in range(len(list_a)):
        if i != '-':
            counter = 1
            for j in range(i + 1, len(list_a)):
                if list_a[i] == list_a[j]:
                    counter += 1
                    list_a[j] = '-'
            if counter > max_counter:
                max_counter = counter
                result = list_a[i]
    print(f'Число {result} встречается {max_counter} раз(а)')


def main():
    start_time = time.time()
    task3_4()
    end_time_1 = time.time()
    print(f'time result: {end_time_1 - start_time}')
    task3_4_v2()
    end_time_2 = time.time()
    print(f'time result: {end_time_2 - end_time_1}')


main()
