def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Traverse through given numbers and increase the count at the absolute value in the hash table
    storage, result = dict(), []
    
    
    # for each element of array
    for n in a:
        storage[n] =  a
        # find the negative value of numbers[n] 
        diff = 0 - n
        # if absolute values are equal to positive numbers
        if diff in storage and diff != 0:
            # store its absolute value in another vector
            result.append(abs(diff))
        
            
    return result


# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# print(has_negatives(list(range(5000000)) + [-1,-2,-3, -5]))
