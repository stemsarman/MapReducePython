"""
    Find and print the balances and jobs of people whose balance is greater than the average balance of blue-collar people.
"""

import sys as s

jobs = []
balances = []

count = 0
total_blue_collar = 0
average_blue_collar = 0

# read each line of the bank.csv file
for line in s.stdin:
    # remove leading and trailing white spaces
    line = line.strip().split('\t')
    
    # read the bank.csv file and store necessary data in appropriate variables
    job = line[0]
    bal = float(line[1])

    # append job to jobs array
    jobs.append(job)
    # append balance to balances array
    balances.append(bal)

    # check for blue-collar job
    if (job == "blue-collar"):
        count = count + 1 
        total_blue_collar = total_blue_collar + bal     # keeping a count of balances of blue-collar jobs

# calculating average of the balances of all blue-collar jobs
average_blue_collar = total_blue_collar / count

print("Average for blue-collar is: ", average_blue_collar)
print("now print balances more than above average!")

# iterating through all the balances which are more than average
for i in range(len(jobs)):
    if (balances[i] > average_blue_collar):
        print(jobs[i], balances[i])     # printing jobs and balances which are more than average
