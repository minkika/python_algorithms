import random

EXAMPLE = [random.randint(0, 100) for _ in range(20)]
print(EXAMPLE)

def odd_indexes(array, result=[]):
    """ Finds indexes of even items in array """
    for index, element in enumerate(array):
        if element % 2 == 0:
            result.append(index)
    return result

print(odd_indexes(EXAMPLE))
