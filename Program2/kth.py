#!/usr/bin/python3

# wrapper for recursive function
def kth_largest(array : list, k : int) -> list:
    if (array == []):
        raise ValueError("Empty list cannot be sorted")

    return kth_rec(array, len(array) - k, 0, len(array) - 1)

# finding middle function
# choosing a "pivot" then making sure everything lower is to its left, and everything greater is to its right
def split(array : list, start : int, end : int) -> int:
    # store a pivot value stored at array[end]
    pivot : int = array[end]

    index : int = start
    pivot_index = start

    while (index <= end - 1):
        if (array[index] <= pivot):
            array[pivot_index], array[index] = array[index], array[pivot_index]
            pivot_index += 1
        index += 1

    array[pivot_index], array[end] = array[end], array[pivot_index]
    return pivot_index


# recursive in class example
def kth_rec(array : list, k_index : int, start : int, end : int) -> int:
    if (start > end):
        return 0

    p = split(array, start, end)

    if (p == k_index):
        return array[k_index]

    if (p > k_index ):
        return kth_rec(array, k_index, start, p - 1)

    return kth_rec(array, k_index, p + 1, end)

def main():
    test = [2, 4, 6, 1, 0]
    k = 2
    print(f"The {k} largest item is {kth_largest(test, k)}.")

if __name__ == "__main__":
    main()
