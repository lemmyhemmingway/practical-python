# pcost.py
#
# Exercise 1.27
# result = 0
# with open('Data/portfolio.csv') as portfolio:
#     for num, line in enumerate(portfolio):
#         if num == 0:
#             continue
#         name, total, price = line.split(',')
#         result += int(total) * float(price)

# print(result)

import csv
import sys

def portfolio_cost(filename):
    result = 0
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File not found")
        return
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:

        name, total, price = row
        result += int(total) * float(price)

    return result

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total_cost = portfolio_cost(filename)
print(total_cost)

