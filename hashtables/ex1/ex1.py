"""
    1. Initialize an empty hash table with dict
    2. For each index in the array:
        - Calculate the pair by subtracting the current list element from the given number (limit)
        - Look up the pair in the hash table
            - If it exists, a pair that is equal to the limit has been found
        - Insert the current index of the array into the hash table after your perform the step above
"""


def get_indices_of_item_weights(weights: list, length: int, limit: int) -> list:
 
    # Your code here
    length = len(weights)
    # Initialize an empty hash table with python dictionary
    hashTable = dict()

    if length <= 1:
        return None

    for i in range(length):
        weight = weights[i]
        if weight in hashTable:
            value = hashTable[weight]
            return [i, value]
        diff = limit - weight
        hashTable[diff] = i
    # if such a pair doesn't exist, return an empty array


    return None
