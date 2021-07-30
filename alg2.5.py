start = 32
stop = 127
numb = 0
for i in range(start, stop + 1):
    numb += 1
    if numb == 10:
        numb = 0
        print(f'{i}:{chr(i)}')
    else:
        print(f'{i}:{chr(i)}', end=" ")

