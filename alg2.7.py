numb = int(input('Введите число '))
num_sum = 0
mult = 0
for i in range(numb):
    num_sum += 1

mult = numb * (numb + 1) / 2

if num_sum == mult:
    print("Равенство 1+2+...+n = n(n+1)/2 верное")
else:
    print("Равенство 1+2+...+n = n(n+1)/2 не верное")
