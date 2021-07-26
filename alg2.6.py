from random import randint

a = randint(0, 100)
shot = 0
while shot != 10:
    num = int(input("Введите число "))
    if num == a:
        print('Вы угадали!')
        break
    elif num > a:
        print(f'Вы ошиблись. Загаданное число меньше {num}. Осталось попыток {10 - shot}')
        shot += 1
    else:
        print(f'Вы ошиблись. Загаданное число больше {num}. Осталось попыток {10 - shot}')
        shot += 1

if shot == 10:
    print(f"Вы проиграли, правильный ответ {a}")
