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

'''
1. What is the best-case scenario?
    The best case scenario is when the partition algorithm returns an index value that is equivalent to (len(array) - client_provided_k)

    This still requires the partition algorithm to place one element. Therefore, the nested while loops will will need to traverse the entire list n times to determine the place to put the pivot value. It does not matter what "k" is selected or what the pivot value is, nor how it relates to the other elements. We will still touch every element to check its value relative to the pivot.

    However, upon returning from the partition function, there is just a comparison between the return index value of partition() and the index value of the kth larget value, when the array is sorted. If this comparison evaluates to true, we just return the value and are done with a best case complexity of O(n).

2. What is the worst-case scenario?
    The worst case scenario would be when a k-value is selected that requires the maximum number of partitions. This means that we are recursively narrowing down which portion of the list the kth largest is in until partition returns an index mathcing len(array) - k, requiring O(log n) time. However, there is still the additional O(n) complexity of the partition function at every recursive call, compounding the total complexity to O(n log n). One thing to note that for the O(n) complexity for partition(), should be on average half as large with each recursive call, because we are narrowing down the search space for the pivot value to be in the correct position.

3. How does the Divide and Conquer aspect of quicksort contribute to it's overall time complexity of O(n log n)?
    Because we divide the problem into 2 functions, one recursive and one iterative, the recursive has a complexity of O(log n), but then on each stack frame, we call a function with O(n) complexity, so we must factor this in, even though the size of n may change. Even if this n is smaller with each recursive call, this reduction in n's size is essentially a fractional coefficient which we'll choose to ignore for significantly large data sets. If the data set were 1 billion items large, the, on average, halfing of the n value when calling partition() will not matter so much, and can still be considered O(n).
'''
