"""
Assume arr is sorted, return True if target is in the array
"""


def binary_search(arr, target):
    # set boundaries for low and high marks to search
    low = 0
    high = len(arr)
    # While low and high do not overlap, check the mid point
    while low <= high:
        mid = (low + high) // 2
    # If it is equal, return True
        if arr[mid] == target:
            return True
    # Else, if target is smaller,
        elif target < arr[mid]:
            # set the high to the mid point value
            high = mid
    # Else, if target is larger,
        else:
            # set the low to the mid point value
            low = mid + 1
    return False
    # If we get to the end, return False (it's not here)


test_list = [5, 3, 7, 33, 845, 218, 432, 745]

print(binary_search(test_list, 33))


def insertion_sort(arr):
    # Divide your hand into sorted on the left, and unsorted on the right
    # Sorted is just the first element
    # Then go card by card and move them into place
    # Loop through all elements in unsorted
    for i in range(1, len(arr)):
        print(arr)
        temp = arr[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j-1]  # slide over one element
            j -= 1
        # Insert at that position
        arr[j] = temp
    return arr


test_arr = [65, 23, 54, 344, 1, 32, 354, 75, 45]

print(insertion_sort(test_arr))

# THIS IS O(n^2) BECAUSE FOR EACH ITEM IN FOR LOOP, YOU WILL BE DOING A WHILE LOOP
