a = input('Введите первую букву ')
b = input('Введите вторую букву ')

start = ord('a') - 1

side_a = ord(a.lower()) - start
side_b = ord(b.lower()) - start
range_ab = side_b - side_a
print(f'В алфавите {a} имеет позицию {side_a}, {b} позицию {side_b}.')
print(f'Колличество букв между ними {range_ab}')
