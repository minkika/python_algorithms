# cycle

def prove_equation(num, left=0):
    """ Counts the left part of eqaution, then the right part and prints results"""
    for i in range(1, num + 1):
        left += i
    right = num * (num + 1) // 2
    return f'{left} == {right}'


print(prove_equation(7))

# recursion

def strange_task(number, left=0, right=1):
    """ Recursively checks the equation """
    if left == right:
        return f'{left} == {right}'
    return strange_task(number, left + 1, number * (number + 1) // 2)


print(strange_task(7))
