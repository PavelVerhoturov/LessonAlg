# создадим словарь для результата
result = {}
for divider in range(2, 10):
    result[divider] = []
    for elem in range(2, 100):
        if elem % divider == 0:
            result[divider].append(elem)
    print(f' {divider}  == {len(result[divider])}')
