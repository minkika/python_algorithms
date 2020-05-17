import random

EXAMPLE = [random.randint(0, 100) for _ in range(20)]
print(EXAMPLE)


def replace_min_max(array):
    """ Replaces minimal and maximal items of array """
    min_i, max_i = 0, 0

    for i in range(len(array)):
        if array[i] < array[min_i]:
            min_i = i
        elif array[i] > max_i:
            max_i = i

    print(f'On index {min_i} is minimal element, {array[min_i]}')
    print(f'On index {max_i} is maximal element, {array[max_i]}')

    array[min_i], array[max_i] = array[max_i], array[min_i]

    return array


print(replace_min_max(EXAMPLE))
