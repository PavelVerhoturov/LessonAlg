from random import randint


def merge(lt_right, lt_left):
    sort_list = []
    lt_left_index = lt_right_index = 0
    for i in range(len(lt_left) + len(lt_right)):
        if lt_left_index < len(lt_left) and lt_right_index < len(lt_right):
            if lt_left[lt_left_index] <= lt_right[lt_right_index]:
                sort_list.append(lt_left[lt_left_index])
                lt_left_index += 1
            else:
                sort_list.append(lt_right[lt_right_index])
                lt_right_index += 1
        elif lt_left_index == len(lt_left):
            sort_list.append(lt_right[lt_right_index])
            lt_right_index += 1
        elif lt_right_index == len(lt_right):
            sort_list.append(lt_left[lt_left_index])
            lt_right_index += 1
    return sort_list


def sort(list_num):
    if len(list_num) <= 1:
        return list_num
    middle = len(list_num) // 2
    list_left = sort(list_num[:middle])
    list_right = sort(list_num[middle:])
    return merge(list_left, list_right)


list_number = [randint(0, 50) for _ in range(15)]
print(f'Исходный массив {list_number}')
print(f'Отсортированный массив {sort(list_number)}')
