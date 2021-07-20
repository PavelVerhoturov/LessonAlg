type = input('Введите раскладку eng или rus ')
a = int(input('Введите номер буквы в алфавите '))

if type == 'eng':
    letter_first = ord('a') - 1
    letter_a = chr(letter_first + a)
    print(f'{a} в {type} раскладке - {letter_a}')
else:
    if type == 'rus':
        letter_first = ord('а') - 1
        letter_a = chr(letter_first + a)
        print(f'{a} в {type} раскладке - {letter_a}')
    else:
        print('Неизветная раскладка')
