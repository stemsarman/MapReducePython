"""
	Count and print the number of times each word occur in file animals.
"""
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split()
	# increase counters
	for word in words:
		# write the resulys to STDOUT  (standard input);
		# what we output here will be the input for the 
		# reduce step, i.e the input for reducer.py
		print('%s\t%s' % (word, 1))