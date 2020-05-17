import random
EXAMPLE = [random.randint(-10, 1) for _ in range(20)]
print(EXAMPLE)

MAX_BEL = -100
MAX_I = 0

for i, el in enumerate(EXAMPLE):
    if el < 0 and abs(el) < abs(MAX_BEL):
        MAX_BEL = el
        MAX_I = i
print(MAX_I, EXAMPLE[MAX_I])
