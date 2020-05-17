from random import random

LOW = input('Enter the lower limit: ')
HIGH = input('Enter the high limit: ')

print('Choose the option: \n1. Random integer \n2. Random float \n3. Random char')
OPTION = int(input('Option: '))

if OPTION == 1:
    RESULT = int(random() * (int(HIGH) - int(LOW) + 1) + int(LOW))
elif OPTION == 2:
    RESULT = random() * (float(HIGH) - float(LOW)) + float(HIGH)
elif OPTION == 3:
    RESULT = chr(int(random() * (ord(HIGH) - ord(LOW) + 1) + ord(LOW)))
else:
    print('Wrong option!')
print(RESULT)
