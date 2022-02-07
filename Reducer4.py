"""
    Find and print average balances of all job types.
"""

import sys as s

dict = {}
# read each line of the bank.csv file
for line in s.stdin:
    # remove leading and trailing white spaces
    line = line.strip().split('\t')

    # read the bank.csv file and store necessary data in appropriate variables
    job = line[0]
    bal = int(line[1])

    # check if job exist in dict and append balance to dict
    if (job in dict):
        dict[job].append(int(bal))
    else:
        dict[job] = []
        dict[job].append(int(bal))
    
# calculate and print average of each job type
for job in dict.keys():
    avg = sum(dict[job]) / len(dict[job])
    print(f'{job}\t{avg}')
