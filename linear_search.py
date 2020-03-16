import random
from datetime import datetime
my_range = 1000000
my_size = 100000

my_random = random.sample(range(my_range), my_size)

# print(my_random)

searching_for = 7


def find_in_number(arr):
    for i in range(len(arr)):
        if my_random[i] == searching_for:
            return True

    return False


def find_value_binary(arr, target):
    if len(arr) <= 1:
        # TODO handle edge
        pass
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        # find middle using integer division
        middle = (first + last) // 2
        if arr[middle] == target:
            found = True
        else:
            if target < arr[middle]:
                # search lower half of remainder
                last = middle - 1
            else:
                # search upper half of remainder
                first = middle + 1
    return found


print("LINEAR:")
start = datetime.now()
print(find_in_number(my_random))
end = datetime.now()
print(f"Runtime: {end - start}")

print(("BINARY:"))
start = datetime.now()
my_random.sort()
print(find_value_binary(my_random, searching_for))
end = datetime.now()
print(f"Runtime: {end - start}")

print(("BINARY AFTER SORT:"))
start = datetime.now()
print(find_value_binary(my_random, searching_for))
end = datetime.now()
print(f"Runtime: {end - start}")
