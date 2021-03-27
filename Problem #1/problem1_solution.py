import numpy as np


def doesArrayContainK(arr, k):
    """Return the two numbers that add up to k
    Parameters:
    argument1 (array): An array of numbers
    argument2 (int): The number k

    Returns:
    Tupple: The two numbers that equals k
    """

    current_val = 0
    for i in arr:
        for j in arr:
            if (i != j):
                current_val = i + j
                if (current_val == k):
                    print("True: " + str(i) + " + " + str(j) + " = " + str(k))
                    return

    if (current_val != k):
        print("False")

###Harcoded example solution 
example_array = [10, 15, 3, 7]

k = 17

doesArrayContainK(example_array, k)

###Random generating numbers
#Create an array with size and containing numbers ranging from lowest to highets
random_array = np.random.randint(low = 1, high = 100, size = 4)

#Find highest possible sum of two numbers in the random array
max = 0
for i in random_array:
    for j in random_array:
        if (i != j):
            current_highest = i + j
            if (max < current_highest):
                max = current_highest

random_k = np.random.randint(low = 1, high = max)

doesArrayContainK(random_array, random_k)