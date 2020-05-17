import random
import timeit

def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array

def bubble_but_better(array):
    n = 1
    while n < len(array):
        count = 0
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
        if count == 0:
            break
        n += 1


array = [random.randint(-100, 100) for _ in range(1000)]
print(array)
bubble_but_better(array)
print(array)


print(timeit.timeit("bubble_but_better(array)", setup="from __main__ import bubble_but_better, array", number=1000))
print(timeit.timeit("bubble_sort(array)", setup="from __main__ import bubble_sort, array", number=1000))

# до доработки
# 10   - 0.01227681600721553
# 100  - 0.596713171020383
# 1000 - 45.94650370799354

# после доработки
# 10   - 0.002983263984788209
# 100  - 0.015837179002119228
# 1000 - 0.11164541501784697

# Доработка ускорила работу алгоритма в много раз
