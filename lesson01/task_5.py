FIRST_LETTER = input("Enter the first letter: ").lower()
SECOND_LETTER = input("Enter the second letter: ").lower()

POS_LEFT = ord(FIRST_LETTER) - ord("a") + 1
POS_RIGHT = ord(SECOND_LETTER) - ord("a") + 1
LENGTH = abs(POS_LEFT - POS_RIGHT) - 1

print(f'The number of {FIRST_LETTER} is {POS_LEFT}')
print(f'The number of {SECOND_LETTER} is {POS_RIGHT}')
print(f'There are {LENGTH} letters between them')
