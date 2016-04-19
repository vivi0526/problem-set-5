#! /urs/bin/env python

#problem 1-1:
import sys
import ipdb
from collections import Counter

filename = 'lamina.bed'

largest_start = 0
chromosome = []

for record in open(filename):
    if record.startswith('#'): continue

    fields = record.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end = fields[2]
    value = fields[3]

    if start > largest_start:
        largest_start = start
        chromosome = chrom

print "answer-1: ", chromosome

#problem1-2:
largest_end = 0
largest_chrom = []
largest_start = 0
largest_value = []
length = 0
for record in open(filename):
    if record.startswith('#'): continue
    fields = record.strip().split('\t')
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    value = fields[3]

    if chrom == 'chrY':
        if end > largest_end:
            largest_end = end
            largest_start = start
            length = end - start
            largest_chrom = chrom
            largest_value = value

print "answer-2: ", chrom, largest_start, largest_end, largest_value, length

#problem 2-1:

filename = 'SP1.fq'

line_num = 0
num_record = 0
largest_c = 0
largest_name = []

for line in open(filename):
    if num_record < 10:
        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()
        elif line_type == 1:
            seq = line.strip()
            if largest_c < Counter(seq)['C']:
                largest_c = Counter(seq)['C']
                largest_name = name
            num_record += 1

        elif line_type == 2:
            quals = line.strip()

        line_num += 1

print "answer-3: ", largest_name

#problem 2-2:
largest_score = 0

line_num = 0
#num_record = 0

for line in open(filename):
    line_type = line_num % 4

    if line_type == 3:
        qual = line.strip()

        score = 0
        for char in qual:
            score += ord(char)

        if score > largest_score:
            largest_score = score

    line_num += 1

print "answer-4: ", largest_score


#problem 2-3:
line_num = 0
num_record = 0
rev_seq = []

def reversed_comp(seq):
    comps = []
    for char in seq:
        if char == 'A':
            comps.append('T')
        elif char == 'T':
            comps.append('A')
        elif char == 'C':
            comps.append('G')
        elif char == 'G':
            comps.append('C')

    return comps

print "answer-5: "

for line in open(filename):
    if num_record < 10:
        line_type = line_num % 4

        if line_type == 1:
            seq = line.strip()
#            ipdb.set_trace()
            rev_seq = reversed_comp(seq)
#            ipdb.set_trace()
            num_record += 1
            print ''.join(reversed(rev_seq))
       # line_num += 1
        line_num += 1


