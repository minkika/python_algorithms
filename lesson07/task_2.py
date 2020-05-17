import random
import timeit


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1

a = [random.randint(0, 49) for i in range (1000)]
print(a)
mergeSort(a)
print(a)

print(timeit.timeit("mergeSort(a)", setup="from __main__ import mergeSort, a", number=1000))

# 10   - 0.03600595297757536
# 100  - 0.29737673301133327
# 1000 - 3.6798999910242856

# Время растет в квадратической зависимости
