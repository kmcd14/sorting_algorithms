# Bubble Sort Algorithm.

# Defining the function.
def bubble_sort(array):
    # Initially assigning True that there will be swapping of elements.
    swap = True
    # While True.
    while swap:
        # Assign False to swap. Prevents having to loop through a sorted array.
        swap = False
        # Getting the last pair of elements (n-2, n-1)
        for element in range(len(array) - 1):
            # If the current element is greater than the next element.
            if array[element] > array[element + 1]:
                # Swap the elements.
                array[element], array[element + 1] = array[element + 1], array[element]
                # Swap becomes True as elements swapped position.
                swap = True
    # Return sorted array.
    return array


# A test array.
an_array = [40, -1, 17, 21, 3, 16]
print(bubble_sort(an_array)) # Calling the function and printing the output.