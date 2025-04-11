#!/usr/bin//python3

# wrapper accepts an array as the sole param
# assume that the array is a python list of integers which has been sorted, then "shifted"
# shift can be any amount left or right or not at all
# returns minimum value in the array
def find_minimum(array: list) -> int:
    if not array:
        return -1

    return find_min_rec(array, 0, len(array) - 1)

#recursively search for the minimum
def find_min_rec(array: list, low: int, high: int) -> int:
    # single element or all of the list has been eliminated
    if low == high:
        return array[low]

    # if the array segment is already sorted
    if array[low] <= array[high]:
        return array[low]

    mid : int = (low + high) // 2

    # find which half to search based on comparison with high element
    if array[mid] > array[high]:
        # min is in the right half
        return find_min_rec(array, mid + 1, high)

    # min is in the left half (including mid)
    return find_min_rec(array, low, mid)

'''
1. Where do we see interval halving at work here?
    The interval halving occurs where we make the recursive calls.
    At this point, we change the values of the low and high paramters based on conditions.
    When mid > high, we know the min value is in the right half
    Otherwise, the minumum has to be in the other half.
    With this method, we only return a value when there is either one item left, or the current section is in sorted order

2. What is the best-case scenario?
    The best case scenario is where the array is sorted and unshifted. array[0] is the min.
    We know this is the case in a subproblem if low is < high.
    When we shift this array [1, 2, 3, 4, 5] to [3, 4, 5, 1, 2]
    array[0] becomes GREATER than array[-1] (last element) and we know the array has been shifted somehow
    This would be O(1) but is relatively unlikely

3. What is the worst-case scenario?
    The worst case scenario would be when the minimum value is at the array position right before or after array[mid]
    It would result in the maximum number of halvings to isolate it to one element we know is the minimum based on our search method.
    This would still be O(log n) though because we're bisecting the list on each recursive call until there's only one item

4. Could this be done using Linear Search?
    It could.
    However, in every situation, we'll have O(n) complexity because we have to touch every item in the list no matter what.
    An example might be:

    def linear_min(array):

        # create a min value variable init to the first element
        min : int = array[0]

        # walk through the entire list from index [0] to [-1]
        for i in range int(len(array)):

            # if an element is less than the current min,
            if (array[i] < min):

                # update min!
                min = array[i]

        # once complete, return the result
        return array[i]

'''
