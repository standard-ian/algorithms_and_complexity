#!/usr/bin/python3

####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 4/18/2025
# CS350 Spring 2025
# Homework 3
#####################################################################
#
# Solution to merge the two arrays into a single sorted array without duplicates.
# Function that takes in array1 and array2 as arguments, and returns the new array containing the merged result
# in ascending sorted order with all duplicate elements removed.
#
# Example:
#   array1 = [1, 2, 4, 5]
#   array2 = [2, 3, 4, 5, 6]
#   The final merged array should be: [1,2,3,4,5,6].
#####################################################################
#

# wrapper function takes 2 arrays, passes each to the recursive function
# then, merges the 2 arrays and removes their duplicates in the same way the recursive function subdivides
def merge_uniq(array1 : list, array2 : list) -> list:
    # stop if both arrays are empty
    if (array1 == [] and array2 == []):
        return []

    # sorting and making each array unique
    array1 = merge_uniq_rec(array1)
    array2 = merge_uniq_rec(array2)

    # merges, removes duplicates across both arrays, returns the merged
    return merge_rm_dupl(array1, array2)

# recursively slices a single array into left and right until only 1 or less elements remain
# then, merges and removes duplicates in the subproblems
def merge_uniq_rec(array : list) -> list:
    # stop if the array is 1 or 0 elements long
    if (len(array) <= 1):
        return array

    # establish a midpoint
    mid = len(array) // 2

    # divede each half in half
    left = merge_uniq_rec(array[:mid])
    right = merge_uniq_rec(array[mid:])

    # recombine, but only include unique elements
    return merge_rm_dupl(left, right)

def merge_rm_dupl(left : list, right : list) -> list:
    #temporary destination to hold unique elements
    temp : list = []

    # establish index trackers and bounds in each list
    left_index : int = 0
    right_index : int = 0
    left_len : int = len(left)
    right_len : int = len(right)

    # while both arrays are in bounds
    while(left_index < left_len and right_index < right_len):

        # the item in the left list at left index is smaller
        # than the right list at right index,
        if (left[left_index] < right[right_index]):

            # if temp array is empty or the current left item is not already present
            if (temp == [] or left[left_index] != temp[-1]):
                #then place it into temp
                temp.append(left[left_index])

            # always increment the left index
            left_index += 1

        # otherwise, place the current smallest element from right into temp if it is unique
        else:
            if (temp == [] or right[right_index] != temp[-1]):
                temp.append(right[right_index])
            right_index += 1

    # if we traversed the entirety of one but not both of the lists
    # append the remaining non-duplicated
    while (left_index < left_len):
        if (temp == [] or left[left_index] != temp[-1]):
            temp.append(left[left_index])
        left_index += 1

    while (right_index < right_len):
        if (temp == [] or right[right_index] != temp[-1]):
            temp.append(right[right_index])
        right_index += 1

    # return the temp array
    return temp

def main():
    array1 = [3, 2, 1]
    array2 = [5, 6, 6, 7]
    print(merge_uniq(array1, array2))

if __name__ == "__main__":
    main()
