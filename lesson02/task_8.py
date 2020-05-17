TIMES = int(input('How many entries do you need: '))
DIGIT = input('Which digit we are to count? ')

COUNTER = 0
for i in range(1, TIMES + 1):
    COUNTER += input(f'Entry {i}: ').count(DIGIT)
print(f'There were {COUNTER} of {DIGIT}')
