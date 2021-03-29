import numpy as np

def productOfAllNumbers(arr):
    """Return a new array with the product of all 
    numbers except for the number at index i

    Parameters:
    argument1 (array): An array with integers

    Return:
    Array: A new array containing the product of all numbers except for i
    """
    result_array = []

    for i in arr:
        sum = 1
        for j in arr: 
            if (i != j):
                sum = sum * j 
        
        result_array.append(sum)
    
    print(result_array)
    return result_array

###Examples
productOfAllNumbers([1, 2, 3, 4, 5])

productOfAllNumbers([3, 2, 1])

#Example with random numbers
random_array = np.random.randint(low = 1, high = 10, size = 4)
productOfAllNumbers(random_array)




