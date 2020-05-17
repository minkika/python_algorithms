def find_max_sum(max_num=0, max_sum=0):
    """ Asks for numbers and finds the largest sum """
    for i in range(1, int(input('Enter how many entries do you need: ')) + 1):
        recent_num = int(input(f'Number {i}: '))
        temp_sum = 0
        temp_num = recent_num
        while temp_num > 0:
            temp_sum += temp_num % 10
            temp_num //= 10
        if temp_sum > max_sum:
            max_sum, max_num = temp_sum, recent_num
    print(f'Max sum {max_sum} were in {max_num}')

find_max_sum()

