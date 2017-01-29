"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith
 entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered
in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other
 punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the
 final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising.
Then post your best test cases to the discussion forums to help your fellow students!

"""

import inversions
import os


file_path = os.path.join('/Users/vishavvk/WebstormProjects/Coursera/Algorithms_Stanford', 'divide_and_conquer', 'week2', 'IntegerArray.txt')

def solution():
    with open(file_path) as f:
        input = [int(line) for line in f]
        _, inversion_count = inversions.sort_and_count(input)
        return inversion_count

print solution()