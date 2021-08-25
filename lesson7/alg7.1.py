from random import randint


def sort_bubble(list_num):
    for i in range(len(list_num)):
        for j in range(len(list_num) - 1):
            if list_num[i] < list_num[j]:
                list_num[i], list_num[j] = list_num[j], list_num[i]
    return list_num


list_number = [randint(-100, 100) for _ in range(15)]
print(f'Исходный массив {list_number}')
print(f'Отсортированный массив {sort_bubble(list_number)}')
