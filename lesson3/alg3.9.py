from random import randint

matrix = []
len_matrix = 10

for i in range(len_matrix):
    cor_row = []
    for j in range(len_matrix):
        elem = randint(0, 99)
        cor_row.append(elem)
    matrix.append(cor_row)

for row in matrix:
    for elem in row:
        print(f'{elem:02}', end=' ')
    print()

min_elems = []

for row in matrix:
    for elem in row:
        min_elems.append(min(elem))

print(max(min_elems))
