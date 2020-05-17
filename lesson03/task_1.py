def find_mults(array, number):
    """ Finds how many items in array are multiples of number"""
    result = []
    for k in array:
        if k % number == 0:
            result.append(i)
    return f' {number}: {len(result)}'


EXAMPLE = [a for a in range(2, 100)]

for i in range(2, 10):
    print(find_mults(EXAMPLE, i))

print('*' * 20)

ANOTHER_ARRAY = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            ANOTHER_ARRAY[j - 2] += 1

for i, item in enumerate(ANOTHER_ARRAY, start=2):
    print(f' {i}: {item}')
