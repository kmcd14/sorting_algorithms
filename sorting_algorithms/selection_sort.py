# Selection Sort Algorithm

# Defining the function.
def selection_sort(array):
    # Outer loop which runs the length of the passed array.
    for element in range(len(array) - 1): 
        # Variable to store the minimum element.
        min_value = element
        # Inner loop which compare the leftmost value to the other values on the right-hand side.
        # Starting at index 1 because the elements before it have already been sorted.
        for current_value in range(element + 1, len(array)):
        # If the selected element is less than the current assigned minumum value.
            if array[current_value] < array[min_value]:
                # It becomes the new minimum value if a swap has occurred.
                min_value = current_value
        # Swapping the minimum element with the first element. 
        array[element], array[min_value] = array[min_value], array[element]     
    # Return sorted array.
    return array


# A test array.
an_array = [22, 14, 27, 6, 3, 16]
print(selection_sort(an_array)) # Calling the function and printing the output.