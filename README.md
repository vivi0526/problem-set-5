# Problem Set 5

| **Due**: 5pm on Apr 19

## Workflow

See [here](https://github.com/MOLB7621/Discussion/issues/9) for the
general workflow.

Your answers should be in YAML format in a file called `answers.yml` at
the top level of the repository.

```
# answers.yml should look like this:
answer-1: 123
answer-2: 456
```

Problem 1 (BED files)
---------------------
Write a Python program to read the lamina.bed file and report the
following:

1. On what chromosome is the region with the largest start position (2nd column) 
   in `lamina.bed`? (**10 points**)

2. What is the region with the largest end position on chrY in
   lamina.bed? (**10 points**) Report as:

   chrom <tab> start <tab> end <tab> value <tab> region_length


Problem 2 (FASTQ files)
-----------------------
Use Python to read the `SP1.fq` file in the `data-sets` repository. Recall that
FASTQ records are comprised of 4 sections; in this case each section will be on
a unique line::

    @cluster_2:UMI_ATTCCG             # record name
    TTTCCGGGGCACATAATCTTCAGCCGGGCGC   # DNA sequence
    +                                 # empty line; starts with '+'
    9C;=;=<9@4868>9:67AA<9>65<=>591   # phred-scaled quality scores

Write a Python program to parse the FASTQ records and report the
following:

3. Which of the first 10 sequence records has the largest number of 'C'
   residues in the sequence? Report its record name (**10 points**).
    
4. For each record, Covert each character in the quality score to a number, and
   sum the numbers. Use the python function `ord` to convert characters to numbers. Report the largest total quality score
   (**10 points**).

5. Report the revese complement of each of the first 10 sequences (**10
   points**). You will have to define a `reverse_complement()` method, or find
   one from another package.

.. note::

    The reverse complement of ``5'-AGCTCGTA-3''`` is ``5'-TACGAGCT-3'``

