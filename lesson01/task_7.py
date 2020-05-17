A = int(input("Enter the first side: "))
B = int(input("Enter the second side: "))
C = int(input("Enter the third side: "))

if A + B <= C or A + C <= B or B + C <= A:
    print("Such triangle does not exist")
elif A != B and A != C and B != C:
    print("It is a miscellaneous triangle")
elif A == B == C:
    print("It is a equilateral triangle ")
else:
    print("It is a isosceles triangle")
