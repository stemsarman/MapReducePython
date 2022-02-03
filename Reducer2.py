"""
    Find account balance of those who are over the age of 30,
    single and have taken a personal loan.
"""

import sys

# read each line from the mapper code output.
for line in sys.stdin:
    # remove leading and trailing white spaces and split the data from the Mapper code
    line = line.strip().split('\t')

    # extract and store the data in appropriate variables from the mapper code output
    age = int(line[0])
    marStatus = line[1]
    ploan = line[2]
    bal = line[3]

    # printing balances of those who are over the age of 30, 
    # single and have taken a personal loan.
    if (age>30 and marStatus == "single" and ploan == "yes"):
        print(bal)
