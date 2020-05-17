import random
import statistics
import timeit

a = [random.randint(0, 100) for i in range(11)]
print(a)
print(statistics.median(a))

def median(array):
    for x in range(len(array)):
        less = 0
        greater = 0
        for y in range(len(array)):
            if x != y:
                if array[x] < array[y]:
                    less += 1
                elif array[x] > array[y]:
                    greater += 1
        if abs(less - greater) <= 1:
            return array[x]

print(median(a))

def large_it(array, total, idx_root):
    largest = idx_root
    left = (2 * idx_root) + 1
    right = (2 * idx_root) + 2
    if left < total and array[left] > array[largest]:
        largest = left
    if right < total and array[right] > array[largest]:
        largest = right
    if largest != idx_root:
        array[idx_root], array[largest] = array[largest], array[idx_root]
        large_it(array, total, largest)


def sort_it(array):
    n = len(array)
    for i in range(n, -1, -1):
        large_it(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        large_it(array, i, 0)

sort_it(a)
print(a[5])

print(timeit.timeit("median(a)", setup="from __main__ import median, a", number=1000))
print(timeit.timeit("sort_it(a)", setup="from __main__ import sort_it, a", number=1000))
print(timeit.timeit("statistics.median(a)", setup="from __main__ import statistics, a", number=1000))

# без сортировки
# 10   - 0.02603523398283869
# 100  - 0.8791736649873201
# 1000 - 182.61604703398189
# захлебнулся на большом массиве

# быстрая сортировка с рекурсией
# 10   - 0.02603523398283869
# 100  - 0.37404972198419273
# 1000 - 5.983183164004004
# рекурсия непропорционально добавляет времени на больших данных
