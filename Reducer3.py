"""
    Find the average balance of blue-collar divorced people.
"""

import sys as s
counter = 0
total = 0
# read each line of the bank.csv file
for line in s.stdin:
    # remove leading and trailing white spaces
    line = line.strip().split('\t')

    # read the bank.csv file and store necessary data in appropriate variables
    bal = int(line[0])
    job = line[1]
    marStatus = line[2]

    # add balance of all blue-collar divorced people
    if (job == "blue-collar" and marStatus == "divorced"):
        counter = counter + 1
        total = bal + total

# print average
print("Average = ", total)