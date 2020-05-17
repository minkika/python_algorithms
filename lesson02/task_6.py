import random

NUM = random.randint(0, 100)
for i in range(1, 11):
    answer = int(input(f'{i} chance: '))
    if answer > NUM:
        print('Less!')
    elif answer < NUM:
        print('More!')
    else:
        print('Yes!')
        break
else:
    print(f'No! that was {NUM}')
