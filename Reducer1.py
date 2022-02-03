"""
    Ques: Find account balance of those who have taken both housing loan and personal loan.
    To run: for Windows users, type the below command.
    'type bank.csv | python Mapper1.py | sort | python Reducer1.py'
"""

import sys

# read each line from the mapper code output.
for line in sys.stdin:
    # remove leading and trailing white spaces and split the data from the Mapper code
    line = line.strip().split('\t')

    # extract and store the data in appropriate variables from the mapper code output
    bal = int(line[0])
    hloan = line[1]
    ploan = line[2]

    # printing balances of people who have taken house loan and personal loan
    if (hloan == "yes" and ploan == "yes"):
        print(bal)
