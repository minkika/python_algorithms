X1 = float(input('Enter the x coordinate of the first point: '))
Y1 = float(input('Enter the y coordinate of the first point: '))
X2 = float(input('Enter the x coordinate of the second point: '))
Y2 = float(input('Enter the y coordinate of the second point: '))

if X1 == X2 and Y1 == Y2:
    print(f'It is a point, infinitely many lines can be drawn')
elif X1 == X2:
    print(f'x = {X1}')
elif Y1 == Y2:
    print(f'y = {Y1}')
else:
    k = (Y2 - Y1) / (X2 - X1)
    B = Y2 - k * X2
    if B == 0:
        print(f'y = {k:.1f}x')
    else:
        print(f'y = {k:.1f}x + {B:.1f}')
