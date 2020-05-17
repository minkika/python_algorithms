# cycle

N = int(input('Enter N: '))
print(f'{2 / 3 * (1 - (-0.5) ** N)}')

def sum_sequence(number):
    """Counts the sum of numerical sequence"""
    result = 0
    delta = 1
    for i in range(number):
        result += delta
        delta *= -0.5
    return result

print(sum_sequence(N))

# recursion

def sum_seq_req(number, result=0.0, start=1.0):
    """ Recursively counts the sum of numerical sequence"""
    if number == 0:
        return result
    return sum_seq_req(number - 1, result + start, start / -2)

print(sum_seq_req(3))
