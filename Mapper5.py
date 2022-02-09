"""
    Find and print the balances and jobs of people whose balance is greater than the average balance of blue-collar people.
"""

import sys as s

# read each line of the bank.csv file
for line in s.stdin:
    # remove leading and trailing white spaces and split bank.csv data
    line = line.strip().split(",")

    # read the bank.csv file and store necessary data in appropriate variables
    job = line[1]
    balance = int(line[5])

    # print the formated data on console
    print(f'{job}\t{balance}')
