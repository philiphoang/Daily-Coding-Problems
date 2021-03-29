import numpy as np 



def findLowestPositiveInteger(arr):
    """Find the lowest positive integer that does not exist in the array

    Parameters:
    argument1 arr: An array with integers

    Return:
    Integer: Lowest possible positive integer that does not exist in the array

    """
    #Sort the array 
    arr.sort()
    
    #Remove any non-positive numbers
    positive_arr = []
    for i in arr:
        if (i >= 1):
            positive_arr.append(i)

    #Initialize the lowest possible value to 1, since it the lowest possible positive integer
    lowest_value = 1

    for i in positive_arr:
        if (lowest_value < i): #Since the array is sorted and we find a smaller number, we can return this value
            return lowest_value

        lowest_value = i + 1

    return lowest_value


example_array = [3, 4, -1, 1]
print(findLowestPositiveInteger(example_array))

example_array1 = [1, 2, 3]
print(findLowestPositiveInteger(example_array1))
