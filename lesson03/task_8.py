EXAMPLE = []

for i in range(1, 5):
    row = []
    summ = 0

    for j in range(1, 5):
        value = int(input(f'String {i}, column {j}: '))
        summ += value
        row.append(value)
    row.append(summ)
    EXAMPLE.append(row)

for line in EXAMPLE:
    for item in line:
        print(f'{item:>5}', end="")
    print()
