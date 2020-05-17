import collections

company = collections.namedtuple('company', ['q1', 'q2', 'q3', 'q4', 'ye'])

companies = {}

n = int(input("Enter number of companies: "))

for i in range(n):
    name = input(f"Name of {i + 1} company: ")
    profit_q1 = int(input('Profit of the 1 quarter: '))
    profit_q2 = int(input('Profit of the 2 quarter: '))
    profit_q3 = int(input('Profit of the 3 quarter: '))
    profit_q4 = int(input('Profit of the 4 quarter: '))
    companies[name] = company(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4,
        ye=profit_q1 + profit_q2 + profit_q3 + profit_q4)

total_profit = 0

for name in companies.keys():
    total_profit += companies[name].ye

result_above = [x for x in companies.keys() if companies[x].ye > (total_profit / n)]
result_below = [x for x in companies.keys() if companies[x].ye <= (total_profit / n)]

print(f"Companies with year profit more than average: {', '.join(result_above)}")
print(f"Companies with year profit less than average: {', '.join(result_below)}")
