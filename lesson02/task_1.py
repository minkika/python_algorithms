# cycle

while True:
    USER_OPERATION = input("Enter operation ( +, -, *, / ) or 0 to exit: ")
    if USER_OPERATION == '0':
        break
    if USER_OPERATION in ('+', '-', '*', '/'):
        X = float(input("x = "))
        Y = float(input("y = "))
        if USER_OPERATION == '+':
            print(f'{X} {USER_OPERATION} {Y} = {(X + Y):.2f}')
        elif USER_OPERATION == '-':
            print(f'{X} {USER_OPERATION} {Y} = {(X - Y):.2f}')
        elif USER_OPERATION == '*':
            print(f'{X} {USER_OPERATION} {Y} = {(X * Y):.2f}')
        elif USER_OPERATION == '/':
            if Y != 0:
                print(f'{X} {USER_OPERATION} {Y} = {(X / Y):.2f}')
            else:
                print("Zero division is not allowed")
    else:
        print("Unknown sign")

# recursion

def calc_recursion():
    """recursive operation input"""
    user_operation = input("Enter operation ( +, -, *, / ) or 0 to exit: ")
    if user_operation == '0':
        return
    if user_operation not in ('+', '-', '*', '/'):
        print("Unknown sign")
        calc_recursion()
    else:
        return calc_operation(user_operation)


def calc_operation(user_operation):
    """ Asks for operands and makes the calculations"""
    user_x = float(input("x = "))
    user_y = float(input("y = "))
    if user_operation == '+':
        print(f'{user_x} {user_operation} {user_y} = {(user_x + user_y):.2f}')
    elif user_operation == '-':
        print(f'{user_x} {user_operation} {user_y} = {(user_x - user_y):.2f}')
    elif user_operation == '*':
        print(f'{user_x} {user_operation} {user_y} = {(user_x * user_y):.2f}')
    elif user_y != 0:
        print(f'{user_x} {user_operation} {user_y} = {(user_x / user_y):.2f}')
    else:
        print("Zero division is not allowed")
        calc_recursion()
    return calc_recursion()


# Run
calc_recursion()
