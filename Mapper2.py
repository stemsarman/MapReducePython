# Find account balance of those who are over the age of 30, single and have taken a personal loan.

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    age = int(line[0])
    marStatus = line[2]
    ploan = line[7]
    bal = line[5]

    print(f'{age}\t{marStatus}\t{ploan}\t{bal}')
