import csv
import random

fields = ['number1', 'number2', 'result']

rows = []

for i in range(20000):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    result = a + b
    rows.append([a, b, result])

filename = 'dataset.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

rows = []

for i in range(1000):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    result = a + b
    rows.append([a, b, result])

filename = 'test.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
