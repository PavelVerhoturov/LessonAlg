my_str = 'Pavel Verhoturov'


def strings(string):
    n = len(string)
    arr_str = set()
    for i in range(1, n):

        for j in range(n - i + 1):

            k = hash(s[j:j+i])

            if k not in arr_str:
                arr_str.add(k)

    return len(arr_str)


print(f'Количество подстрок: {strings(my_str)}')