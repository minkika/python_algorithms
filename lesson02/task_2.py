# cycle

def count_evens_with_arithmetic(number):
    """ Counts odd and even ts in number """
    evens, odds = 0, 0
    while number > 0:
        if (number % 10) % 2 == 0:
            evens += 1
        else:
            odds += 1
        number //= 10
    return f'Evens: {evens}, odds: {odds}'

def count_evens(str_number):
    """ Counts evens in user input number"""
    evens = 0
    for digit in str_number:
        if int(digit) in (0, 2, 4, 6, 8):
            evens += 1
    return f'Evens: {evens}, odds: {len(str_number) - evens}'

print(count_evens_with_arithmetic(12345))

USER_INPUT = '12345'
print(count_evens(USER_INPUT))

EVEN_ARRAY = [a for a in USER_INPUT if int(a) % 2 == 0]
print(f'Evens: {len(EVEN_ARRAY)}, odds: {len(USER_INPUT) - len(EVEN_ARRAY)}')

# recursion

def count_odds(num, odds=0, evens=0):
    """ Recursively checks each last digit to be odd """
    if num == 0:
        return f'There are {odds} odds and {evens} evens'
    if num % 2:
        return count_odds(num // 10, odds, evens + 1)
    return count_odds(num // 10, odds + 1, evens)

print(count_odds(1234))
print(count_odds(98765456789))
print(count_odds(989))