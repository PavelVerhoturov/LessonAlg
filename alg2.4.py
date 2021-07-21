l = 2
m = 0
n = int(input())

while n != 0:
    m = m + l / 2
    l /= 2
    n -= 1

print(m)
