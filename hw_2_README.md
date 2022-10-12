# Python_BI_2022

This repository contains the homeworks for the Python course (September-December, 2022) in the Bioinformatics Institute.

## Homework_2

Homework 2 contains program that processes files in .fastq format. Utilite enables to filter sequences based on GC-content and mean quality of the reads.

### Launch program

To launch the utility download .py scripts and run the program in terminal using `python3 collection_hw.py` command.

#### Program arguments

Program accepts the following arguments:

`input_fastq` --- path to the input file; 

`output_file_prefix` --- prefix for the output file: *_passed.fastq* for the file with reads passed the filter, *_failed.fastq* for the file with reads that did not passed the filter;

`gc_bounds` --- percentage interval of guanine-cytosine content. One entered number takes it as an upper limit, default interval is (0, 100);

`length_bound` --- length interval for filtration, default interval is (0, 2<sup>32</sup>);

`quality_threshold` --- limit for the mean value of read quality; 

`save_filtered` --- whether filtered reads would be saved or not; default is **False**. 
