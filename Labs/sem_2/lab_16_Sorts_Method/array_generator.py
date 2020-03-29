import random

def get_sorted_arr(size):
    return [i for i in range(0, size, 1)]

def get_reversed_sorted_arr(size):
    return [i for i in range(size, 0, -1)]

def get_random_arr(size):
    random.seed()
    return [random.randint(-size, size) for i in range(size, 0, -1)]