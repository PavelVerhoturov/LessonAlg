matrix = []
len_matrix = 4

# генерация матрицы
for i in range(len_matrix):
    cor_row = []
    for j in range(len_matrix):
        elem = int(input('Введите натуральное число: '))
        cor_row.append(elem)
    matrix.append(cor_row)

for row in matrix:
    sum_row = 0
    for elem in row:
        sum_row += elem
        print(f'{elem:03}', end=' ')
    print(f'{sum_row:03}')
