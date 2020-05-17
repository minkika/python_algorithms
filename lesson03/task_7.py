import random

EXAMPLE = [random.randint(0, 100) for _ in range(20)]
print(EXAMPLE)

if EXAMPLE[0] > EXAMPLE[1]:
    MIN_I_1 = 0
    MIN_I_2 = 1
else:
    MIN_I_1 = 1
    MIN_I_2 = 0

for i in range(2, len(EXAMPLE)):
    if EXAMPLE[i] < EXAMPLE[MIN_I_1]:
        a = MIN_I_1
        MIN_I_1 = i
        if EXAMPLE[a] < EXAMPLE[MIN_I_2]:
            MIN_I_2 = a
    elif EXAMPLE[i] < EXAMPLE[MIN_I_2]:
        MIN_I_2 = i

print(f'On index {MIN_I_1} is minimal element, {EXAMPLE[MIN_I_1]}')
print(f'On index {MIN_I_2} is the second minimal element, {EXAMPLE[MIN_I_2]}')
