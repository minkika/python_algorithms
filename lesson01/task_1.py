THREE_DIGITS_NUMBER = int(input('Enter a three digit number: '))
A = THREE_DIGITS_NUMBER // 100
B = THREE_DIGITS_NUMBER % 100 // 10
C = THREE_DIGITS_NUMBER % 10

print(f'The sum of digits: {A + B + C}')
print(f'The mult of digits: {A * B * C}')
