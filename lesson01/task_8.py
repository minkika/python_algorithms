Y = int(input('Enter the year: '))

if Y % 4 != 0 or (Y % 100 == 0 and Y % 400 != 0):
    print("Not leap year")
else:
    print("Leap year")

print('Not leap' if Y % 4 != 0 or (Y % 100 == 0 and Y % 400 != 0) else 'Leap')
