import time
import math

def not_erato(n):
    list_1 = [2]
    num = 3
    counter = 1
    while counter < n:
        f = True
        for elem in list_1:
            if num % elem == 0:
                f = False
                break
        if f == True:
            counter += 1
            list_1.append(num)
        num += 1
    return list_1


def prime(n):
    counter_prime = 0
    counter_number = n
    while counter_prime <= n:
        counter_prime = counter_number / math.log(counter_number)
        counter_number += 1
    return counter_number


def erato(n):
    end = prime(n)
    list_1 = [_ for _ in range(2, end)]
    lst = len(list_1)
    for elem in list_1:
        if elem != 0:
            for number in range(elem, lst, elem):
                list_1[number] = 0
    list_2 = [x for x in list_1 if x != 0]
    return list_2


def main():
    start_time = time.time()
    erato(1000)
    end_time_1 = time.time()
    print(f'erato: {end_time_1 - start_time}')
    not_erato(1000)
    end_time_2 = time.time()
    print(f'not_erato: {end_time_2 - end_time_1}')


main()
