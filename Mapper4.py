"""
    Find and print average balances of all job types.
"""

import sys as s

# read each line of the bank.csv file
for line in s.stdin:
    # remove leading and trailing white spaces and split bank.csv data
    line = line.strip().split(",")

    # read the bank.csv file and store necessary data in appropriate variables
    job = line[1]
    bal = int(line[5])

    # print the formated data on console
    print(f'{job}\t{bal}')
