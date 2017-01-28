"""Count the inversions in the array.
Problem Statement:
Input: An array containing number 1, 2, 3,.. in any arbitrary order
Ouput: no. of inversions such that A[i] > A[j] where i > j.

Example: Given input array: [1, 3, 5, 2, 4, 6]
Output will be: 3 = (3,2), (5, 2), (5, 4)
Motivation:
numerical similarity between two ranked lists. Collaborative filtering.
For eg: finding similarity in the fav movie lists given by two people.
"""

def brute_force(input):
    inversions = 0
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            inversions += bool(input[i] > input[j])
    return inversions

def test_inversions(f):
    assert f([1, 2, 3]) == 0
    assert f([1]) == 0
    assert f([1, 3, 5, 2, 4, 6]) == 3
    assert f([6, 5, 4, 3, 2, 1]) == 15

test_inversions(brute_force)

# O(nlogn) solution
"""
Basic premise of this solution:
let n be length of array
if n is 1 then inversions = 0
otherwise divide the array.
count inversions on the left side, count inversions on the right side,
and then count inversions on the splitarray (or in other words the merged array)
sum of all three counts is the inversion returned.

Goal: implement count of split inversions in linear time O(n) time then count
will run in O(nlogn) time.

Implementation:
Key ID: have recursive calls both count inversions and sort using merge sort.
"""

def sort_and_count(input):
    size = len(input)
    if size <= 1:
        return input, 0
    left_array, left_count = sort_and_count(input[:size/2])
    right_array, right_count = sort_and_count(input[size/2:])
    merged_array, split_count = merge_and_count_split(left_array, right_array)
    return merged_array, left_count + right_count + split_count

# takes in two sorted arrays
def merge_and_count_split(in1, in2):
    output, i, j, l1, l2 = [], 0, 0, len(in1), len(in2)
    inversion_count = 0
    while i < l1 and j < l2:
        if in1[i] < in2[j]:
            output.append(in1[i])
            i += 1
        else:
            output.append(in2[j])
            j += 1
            # because all the remaining elements are greater than this element.
            inversion_count += l1 - i
    # copy over leftovers
    output += in1[i:]
    output += in2[j:]
    return output, inversion_count

def test_merge_and_count_split(f):
    assert f([1, 2, 3], [4, 5, 6]) == ([1, 2, 3, 4, 5, 6], 0)
    assert f([1, 3, 5], [2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3)
    assert f([1], [2]) == ([1, 2], 0)

test_merge_and_count_split(merge_and_count_split)

def test_sort_and_count(f):
    assert f([1, 2, 3]) == ([1, 2, 3], 0)
    assert f([1]) == ([1], 0)
    assert f([1, 3, 5, 2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3)
    assert f([6, 5, 4, 3, 2, 1]) == ([1, 2, 3, 4, 5, 6], 15)

test_sort_and_count(sort_and_count)

"""
Following also returns the inversions that happened.
As you will notice finding inversions that happened isn't optimized.
We have increased the complexity to O(n^2)
"""
def sort_and_count_with_inv(input):
    size = len(input)
    if size <= 1:
        return input, 0, []
    left_array, left_count, left_inversions = sort_and_count_with_inv(input[:size/2])
    right_array, right_count, right_inversions = sort_and_count_with_inv(input[size/2:])
    merged_array, split_count, split_inversions = merge_and_count_split_with_inv(left_array, right_array)
    return merged_array, left_count + right_count + split_count, left_inversions + right_inversions + split_inversions

# takes in two sorted arrays
def merge_and_count_split_with_inv(in1, in2):
    output, i, j, l1, l2 = [], 0, 0, len(in1), len(in2)
    inversion_count = 0
    inversions = []
    while i < l1 and j < l2:
        if in1[i] < in2[j]:
            output.append(in1[i])
            i += 1
        else:
            output.append(in2[j])
            inversions += [(in1[x], in2[j]) for x in range(i, l1)]
            j += 1
            # because all the remaining elements are greater than this element.
            inversion_count += l1 - i

    # copy over leftovers
    output += in1[i:]
    output += in2[j:]
    return output, inversion_count, inversions

print sort_and_count_with_inv([1, 3, 5, 2, 4, 6])

def test_sort_and_count_with_inv(f):
    assert f([1, 2, 3]) == ([1, 2, 3], 0, [])
    assert f([1]) == ([1], 0, [])
    assert f([1, 3, 5, 2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3, [(3, 2), (5, 2), (5, 4)])
    # assert f([6, 5, 4, 3, 2, 1]) == ([1, 2, 3, 4, 5, 6], 15)

# test_sort_and_count_with_inv(sort_and_count_with_inv)