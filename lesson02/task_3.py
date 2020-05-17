# cycle

def mirror_number(number):
    """ Cyclically adds the last digit to empty string """
    result = ''
    while number > 0:
        result += str(number % 10)
        number //= 10
    return result

def mirror_cycle(number):
    """ Cyclically adds the last digit to empty string"""
    result = ''
    for i in number:
        result = f'{i}{result}'
    return result

def mirror_array(number):
    """ Back slice of string"""
    return number[::-1]

print(mirror_number(12345))

USER_INPUT = '12345'
print(mirror_array(USER_INPUT))
print(mirror_cycle(USER_INPUT))

# recursion

def reverse_num(num):
    """ Recursively adds the last digit to empty string"""
    if num == 0:
        return ""
    return str(num % 10) + (reverse_num((num // 10)))


print(reverse_num(12345))
