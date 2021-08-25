from random import randint


def median(list_num, middle):
    if len(list_num) == 0:
        return list_num
    if len(list_num) == 1:
        return list_num[0]

    list_left = []
    list_right = []
    step = []
    for i in list_num:
        if i < list_num[0]:
            list_left.append(i)
        elif i > list_num[0]:
            list_right.append(i)
        else:
            step.append(i)

    if len(list_left) > middle:
        return median(list_left, middle)
    elif len(list_left) + len(step) > middle:
        return step[0]
    else:
        return median(list_right, middle - len(list_right))

m = 7
list_number = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив {list_number}')
print(f'Медиана {median(list_number, m)}')
