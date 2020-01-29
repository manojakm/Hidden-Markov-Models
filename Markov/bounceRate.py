import numpy as np

transitions = {}

row_sums = {}

# read all the rows in file and create transitions dictions having start and end combo
#  as key and count as value.
for line in open('site_data.csv'):
    s,e = line.rstrip().split(',')
    transitions[(s,e)] = transitions.get((s,e), 0.) + 1
    row_sums[s] = row_sums.get(s, 0.) + 1

print(row_sums)
transitions.items()

# find probabilities from counts
for k,v in transitions.items():
    s, e = k
    transitions[k] = v / row_sums[s]

# look for initial states (where start page is not there i.e. -1)
for k,v in transitions.items():
    s, e = k
    if (s == '-1'):
        print((k,v))

# find all bounced pages

for k,v in transitions.items():
    s, e = k
    if (e == 'B'):
        print((s, v))


     