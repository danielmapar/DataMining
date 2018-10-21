#!/usr/bin/env python
import sys
import math
import statistics
import csv

def z_score(values):

    mean = statistics.mean(values)
    n = len(values)

    standard_deviation = math.sqrt(
        (1/(n-1)) *
        sum([
            math.pow((value - mean), 2) for value in values
        ])
    )

    zscore_normalization = [
        float("{0:.4f}".format(
            (value - mean)/(standard_deviation)
        )) for value in values
    ]

    return zscore_normalization

file = ""

if len(sys.argv) > 1:
    file = open(sys.argv[1])
else:
    file = open("input.txt")

tuples = []
normalized_tuples = []

print("Tuples: ")

for line in file:
    print(line.split())
    tuples.append([ float(x) for x in line.split()])


num_cols = len(tuples[0])

for col_index in range(num_cols):
    column_vals = [tuple[col_index] for tuple in tuples]
    normalized_tuples.append(z_score(column_vals))

normalized_tuples = zip(*normalized_tuples)

print("Normalized tuples: ")
[print(normalized_tuple) for normalized_tuple in normalized_tuples]

with open('output.txt', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerows(normalized_tuples)
