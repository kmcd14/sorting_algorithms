# Insertion Sort Algorithm

# Defining the function.
def insertion_sort(array):
    # Outer loop which runs from index 1 to the last element.
    # Starting at index 1 because we assume the element at index 0 is in the correct position.
    for index in range(1, len(array)):
        # Temporary variable to keep track of the current index.
        current_value = array[index]
        # Variable to hold an elements correct position.
        position = index
        # Inner loop to find an element’s correct position.
        # While the current element is less than the next element. 
        while position > 0 and array[position - 1] > current_value:
            # Shifts elements down (right) an index to make space for the next element.
            array[position] = array[position - 1]
            # Moving to the next element 
            position = position - 1
        # Putting elements at the correct index when found.
        array[position] = current_value
    # Return the sorted array.
    return array


# A test array.
an_array = [27, 14, -1, -10, 3, 16]
print(insertion_sort(an_array)) # Calling the function and printing the output.


