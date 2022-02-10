"""
    Find account balance of those who are over the age of 30,
    single and have taken a personal loan.
"""

import sys

# read each line of the bank.csv file
for line in sys.stdin:
    # remove leading and trailing white spaces and split bank.csv data
    line = line.strip().split(",")

    # read the bank.csv file and store necessary data in appropriate variables
    age = int(line[0])
    marStatus = line[2]
    ploan = line[7]
    bal = line[5]

    # print the formated data on console
    print(f'{age}\t{marStatus}\t{ploan}\t{bal}')
