# Find account balance of those who have taken both housing loan and personal loan.

import sys

# read each line of the bank.csv file
for line in sys.stdin:
    # remove leading and trailing white spaces and split bank.csv data
    line = line.strip().split(",")

    # read the bank.csv file and store necessary data in appropriate variables
    bal = int(line[5])
    hloan = line[6]
    ploan = line[7]
    
    # print the formated data on console
    print(f'{bal}\t{hloan}\t{ploan}')
    