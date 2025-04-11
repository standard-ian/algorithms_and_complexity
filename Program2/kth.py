#!/usr/bin/python3

####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 4/10/2025
# CS350 Spring 2025
# Homework 2
#####################################################################
# implementation of function to find the k-th largest value in an unsorted list of integers
# k is a quantifier from largest. i.e. in [1, 2, 3], 3 is the 1st largest, 2 is the 2nd largest, etc.
# index of "k-th" largest is k from the end or index [len(array) - k]
# duplicates, positives, invalid k should all be dealt
#####################################################################
#

# wrapper for recursive function
# params: list of integers, "k-th" largest value
# returns: the "k-th" largest value
def kth_largest(array : list, k : int) -> list:
    #raise exceptions if empty or k is invalid
    if (array == []):
        raise ValueError("Empty list cannot be sorted")
    array_len = len(array)
    if (k < 1 or k > array_len):
        raise ValueError("k out of range")

    # call recursive function
    # redefine k as the index of k
    # bounds: index first-last
    return kth_rec(array, array_len - k, 0, array_len - 1)

# finding middle function, helper for kth_largest
# choosing a "pivot" then making sure everything lower is to its left, and everything greater is to its right
def partition(array : list, start : int, end : int) -> int:
    # store a pivot value stored at array[end]
    pivot : int = array[end]

    # establish position trackers at start of sub-problem
    index : int = start
    pivot_index = start

    # this loop does not include the pivot
    while (index <= end - 1):
        # if an item should be to pivot's left, move it
        if (array[index] <= pivot):
            # swap items at the position trackets
            array[pivot_index], array[index] = array[index], array[pivot_index]
            # increment if a swap occured
            pivot_index += 1

        # always increment index
        index += 1

    # after pivot index is correctly set, swap it with the actual pivot
    array[pivot_index], array[end] = array[end], array[pivot_index]

    return pivot_index


# recursive function using partition to find the kth largest
# base case is that we find a kth largest, one has to exist now
# wrapper eliminates chance of empty list or invalid k
def kth_rec(array : list, k_index : int, start : int, end : int) -> int:

    # use partition on each recursive call to find a "middle" value
    p = partition(array, start, end)

    # if on this stack frame, the partition "center" is placed correctly relative to other values
    # return the value, it is the kth largest
    if (p == k_index):
        return array[k_index]

    # determine to continue searching and partitioning in upper or lower half
    if (p > k_index ):
        return kth_rec(array, k_index, start, p - 1)
    return kth_rec(array, k_index, p + 1, end)

def main():
    test = [2, 4, 6, 1, 0]
    k = 2
    print(f"The array before:  {test}")
    print(f"The {k} largest item is {kth_largest(test, k)}.")
    print(f"The array after:  {test}")

if __name__ == "__main__":
    main()
