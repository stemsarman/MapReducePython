import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')

    age = int(line[0])
    marStatus = line[1]
    ploan = line[2]
    bal = line[3]

    if (age>30 and marStatus == "single" and ploan == "yes"):
        print(bal)
