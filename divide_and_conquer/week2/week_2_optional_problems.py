"""
The following problems are for those of you looking to challenge yourself beyond the required problem sets and
programming questions. Most of these have been given in Stanford's CS161 course, Design and Analysis of Algorithms,
at some point. They are completely optional and will not be graded. While they vary in level, many are pretty
challenging, and we strongly encourage you to discuss ideas and approaches with your fellow students on
the "Theory Problems" discussion form.
"""

"""
Problem 1:
You are given as input an unsorted array of n distinct numbers, where n is a power of 2. Give an algorithm that
identifies the second-largest number in the array, and that uses at most n + log2n - 2 comparisons.

Reading: Proof here: http://jeffe.cs.illinois.edu/teaching/497/02-selection.pdf
"""
import merge_sort

## Naive approach is to sort and then find the second element this will take O(nlogn) time.
## this can be done in O(n)time.
def SecondLargedNumber_Naive(input):
    sorted_array = merge_sort.merge_sort(input)
    return sorted_array[-2]

def SecondLargestNumber(input):
    """
    No need for sorting the array.
    :param input:
    :return:
    """
    max_value = input[0]
    second_max = 0
    for x in input:
        if x > max_value:
            second_max = max_value
            max_value = x
        elif second_max < x != max_value:
            second_max = x
    return second_max



def testSecondLargedNumber(f):
    # assert f([96, 2, 1]) == 2
    assert f([1, 2, 3, 4]) == 3
    assert f([1, 2, 3, 4, 5, 6]) == 5
    assert f([2, 1, 3, 6, 5, 4]) == 5

testSecondLargedNumber(SecondLargedNumber_Naive)

testSecondLargedNumber(SecondLargestNumber)


"""
Problem 2:
You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until
its maximum element, after which its elements are in decreasing order. Give an algorithm to compute the maximum element
 that runs in O(log n) time.
"""

def FindMaxiumElement_Linear(input):
    max_element = input[0]
    for x in input[1:]:
        if max_element < x:
            max_element = x
        else:
            # Since its unimodal no need to proceed further.
            break
    return max_element


def testFindMaxiumElement(f):
    assert f([1, 2, 3, 4, 5, 4, 3]) == 5
    assert f([6, 7, 8, 9, 3, 2, 1]) == 9
    assert f([1, 2, 3, 1]) == 3

testFindMaxiumElement(FindMaxiumElement_Linear)

def FindMaxElementOptimized(input):
    """
    This is O(logn) comparison
    T(n) = T(n/2) + O(1)
    i.e. a = 1, b = 2, d = 0
    so O(n^dlogn) = O(logn)
    :param input:
    :return:
    """
    size = len(input)
    if size == 0:
        return
    if size == 1:
        return input[0]
    left_half = input[:size/2]
    right_half = input[size / 2:]
    half_selected = []
    # Since the array is unimodal, we can ignore one half.
    if left_half[-1] > right_half[0]:
        half_selected = left_half
    else:
        half_selected = right_half
    # So we only recurse on one half at any given time.
    return FindMaxElementOptimized(half_selected)


# print FindMaxElementOptimized([6, 7, 8, 9, 3, 2, 1])

testFindMaxiumElement(FindMaxElementOptimized)

"""
Problem 3:
You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or
 zero. You want to decide whether or not there is an index i such that A[i] = i.
 Design the fastest algorithm that you can for solving this problem.
"""

def BruteForceMatchingIndexElement(input):
    """
    This is linear time O(n)
    :param input:
    :return:
    """
    for x in range(len(input)):
        if x == input[x]:
            return x
    return -1

def testMatchingIndexElement(f):
    assert f([1, 2, 3, 4, 5, 6]) == -1
    assert f([0, 1, 2, 3, 4, 5]) == 0
    assert f([-1, 0, 2, 3, 4, 5]) == 2


def OptimizedMatchingElement(input):
    for x in range(len(input)):
        if x == input[x]:
            return x
        if x < input[x]:
            # Optimization which takes into account the property of the input array.
            # So we only check up until we hit a point when index becomes smaller than the element in the array
            break
    return -1


testMatchingIndexElement(BruteForceMatchingIndexElement)

testMatchingIndexElement(OptimizedMatchingElement)

"""
Problem 4:
You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its
 neighbors. (A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four
  neighbors; numbers on the side have three; the four corners have two.) Use the divide-and-conquer algorithm design
   paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers. (Note: since there are n2
    numbers in the input, you cannot afford to look at all of them. Hint: Think about what types of recurrences would
    give you the desired upper bound.)
"""