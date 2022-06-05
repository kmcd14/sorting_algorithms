# Counting Sort Algorithm

# Defining the function.
def counting_sort(array):
     # An array to store the frequency each unique element appears.
     # Getting the biggest element in the array + 1. E.g. if it was 5 it would be 6.
    count = [0] * (max(array) + 1)
     # A new array which will overwrite the unsorted inputted array. 
    sorted = [0] * len(array)
    # For each element in the array.
    for element in array:
        # Count the number of times it appears.
        count[element] += 1  
    # For each element in the count array (keeping track of an elements frequency).
    for value in range(1, len(count)):
        # Putting the elements in the correct position.
        count[value] += count[value - 1] 
    # Constructing the sorted array. 
    # For each element in the original array.
    for element in array:
        # Overwrite the original input with the elements correct position. Decrease by -1.
        sorted[count[element] - 1] = element
    # Return sorted array.
    return sorted


# A test array.
an_array = [3, 70, 1, 13, 33]
print(counting_sort(an_array)) # Calling the function and printing the output.