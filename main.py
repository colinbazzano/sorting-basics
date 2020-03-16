import random


# def my_for_loop(n):
#     print(n)

# my_for_loop(10)

# my_range = 1000
# my_size = 1000

# my_random = random.sample(range(my_range), my_size)

# # # print(my_random)


# # def print_number(n, arr):
# #     print(arr[n])


# # print_number(4, my_random)

# def print_array(arr):
#     for i in range(len(arr)):
#         print(arr[i])

# print_array(my_random)

animals = ["Duck", "Sheep", "Cat", "Dog", "Tiger", "Fox", "Giraffe"]


# def print_animals(list):
#     my_number = 0
#     for i in range(len(list)):
#         print(list[i])
#         for _ in range(1000):
#             my_number += 1


# print_animals(animals)

# def print_animal_pairs():
#     for animal_1 in animals:
#         for animal_2 in animals:
#             print(f"{animal_1} - {animal_2}")


# print_animal_pairs()

# def print_animal_triplets():
#     for animal_1 in animals:
#         for animal_2 in animals:
#             for animal_3 in animals:
#                 print(f"{animal_1}-{animal_2}-{animal_3}")


# print_animal_triplets()

def get_animal_combos(list):
    list_length = len(list)
    if list_length == 0:
        return [[]]
    else:
        animal_combos = []
        previous_combos = get_animal_combos(list[1:])
        for combo in previous_combos:
            animal_combos.append(combo)
            animals.append(combo + [list[0]])
        return animal_combos


print(get_animal_combos(animals))
