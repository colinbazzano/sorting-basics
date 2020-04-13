my_list = ['Joe', 2, 'Ted', 4.98, 14, 'Sam',
           'void *', '42', 'float', 'pointers', 5006]

# 1. assign the list to a variable to perform on it

# loop through and for each, print the element
for el in my_list:
    print(el)


my_int_list = [3, 1, 3, 1, 5, 7, 3]


def add_nums(arr):
    total = 0
    for el in arr:
        total = total + el
    return total


def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    for i in a, b:
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
        else:
            return
    return [alice_points, bob_points]


alice = [1, 5, 3]
bob = [5, 2, 1]

print(compareTriplets(alice, bob))
