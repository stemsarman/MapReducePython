"""
    Find the average balance of blue-collar divorced people.
"""

import sys as s

# read each line of the bank.csv file
for line in s.stdin:
    # remove leading and trailing white spaces and split bank.csv data
    line = line.strip().split(",")
    
    # read the bank.csv file and store necessary data in appropriate variables
    bal = int(line[5])
    job = line[1]
    marStatus = line[2]

    # print the formated data on console
    print(f'{bal}\t{job}\t{marStatus}')
    