# Write a linear search algorithm


def linear_search(arr, item):
    for i in arr:
        if arr[i] == item:
            return i
    return False


# Write a binary search algorithm
test_array = [1, 4, 5, 7, 3, 54]
print(linear_search(test_array, 3))


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:  # While you haven't narrowed it down to one element
        mid = (low + high) // 2  # check the middle element
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            # the guess is greater than the item, so the RHS list is excluded, and the high is the middle index minus one (the largest number in the LHS list)
            high = mid - 1
        else:  # the opposite is true, so the LHS is eliminated and the low is now the lowest number in the RHS list
            low = mid + 1
    return None  # if we never find it


test_list = [4, 1, 5, 3, 84, 24, 63, 45, 74, 92, 455, 53]

print(binary_search(test_list, 24))
