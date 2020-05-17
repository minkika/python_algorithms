# cycle

for i in range(32, 128):
    print(f'\t{i} - {chr(i)}', end=' ')
    if i % 10 == 1:
        print('')

# recursion

def ascii_digits(n):
    """ Recursively PRINTS the charset """
    if n != 128:
        print(f'{n} - {chr(n)}', end=' ')
        if n % 10 == 1:
            print()
        return ascii_digits(n + 1)

ascii_digits(32)
