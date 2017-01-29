# Implementation of merge sort.
def merge(in1, in2):
    output, i, j, l1, l2 = [], 0 , 0, len(in1), len(in2)
    while i < l1 and j < l2:
        if in1[i] < in2[j]:
            output.append(in1[i])
            i += 1
        else:
            output.append(in2[j])
            j += 1

    output += in1[i:]
    output += in2[j:]

    return output

def test_merge():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 4], [2, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 2], [4, 5, 6]) == [1, 2, 4, 5, 6]
    assert merge([4], [1, 2, 6, 7]) == [1, 2, 4, 6, 7]
    assert merge([], []) == []

test_merge()


# takes an unsorted array and outputs a sorted array
def merge_sort(input):
    size = len(input)
    if size <= 1:
        # array is already sorted no need to do anything
        return input
    return merge(merge_sort(input[:size//2]), merge_sort(input[size//2:]))


def test_merge_sort():
    assert merge_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([7, 8, 1, 2]) == [1, 2, 7, 8]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]

test_merge_sort()