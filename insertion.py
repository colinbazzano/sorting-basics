# This file is for insertion sort! All things regarding that can be found below

"""insertion sorting
left side first index is "sorted"
think of it in this process:
8|2?
2, 8 | 3?
2, 3, 8 | 5?
2, 3, 5, 8 | 4?
2, 3, 4, 5, 8

Each time you are shifting the numbers one at a time to get your number? to be in the right spot
"""
my_list = [8, 2, 3, 5, 4, 1, 24, 29, 15, 93, 92, 430, 43, 22, 92, 15]

print("my list:", my_list)


def insertion_sort(list_to_sort):
    # separate first element, think of it as sorted

    # for all other indices, starting at 1
    for i in range(1, len(list_to_sort)):
        # put current number in a temp variable
        temp = list_to_sort[i]
        # look left, until we find where it belongs
        j = i
        while j > 0 and temp < list_to_sort[j-1]:

            # as we look left, shift items to the right as we iterate
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1

        # when left is smaller than temp, or we're at zero, put temp at this spot
        list_to_sort[j] = temp

    return list_to_sort


print(insertion_sort(my_list))
