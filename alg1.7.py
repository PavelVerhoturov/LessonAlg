a = int(input("Введите первую сторону треугольника "))
b = int(input("Введите вторую сторону треугольника "))
c = int(input("Введите третью сторону треугольника "))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b or b == c or c == a:
        print('Треугольник равнобедренный')
    else:
        if a == b and b == c and c == a:
            print('Треугольник равносторонний')
        else:
            print('Треугольник разносторонний')
else:
    print('Треугольника не существует')