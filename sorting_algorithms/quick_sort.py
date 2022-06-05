# QuickSort Algorithm

# Defining a function.
def quick_sort(array):
    # Divide and conquer.
    
    less = [] # Empty array for elements less than pivot (left).
    greater = [] # Empty array for elements greater than pivot (right).
    equal = [] # Empty array for elements equal to pivot (centre).

    # Outer loop.
    # Base case. If the length of the array is less than or equal to 1.
    if len(array) <= 1:
        # Return original array.
        return array
    # If the length of the array is greater than 1.
    else:
        # Use the first element as the pivot.
        pivot = array[0]
        # For each element in the array.
        for element in array:
            # If the element is less than the pivot.
            if element < pivot:
                # Add it to the less array (left-hand side)
                less.append(element)
            # If the element is greater than the pivot.
            elif element > pivot:
                # Add it to the greater array (right-hand side)
                greater.append(element)
            else:
                # Otherwise add the element to the equal array.
               equal.append(element)
        # Use recursion by recalling the quick_sort() function to sort the less and greater arrays.
        # Return sorted array by putting the divided arrays back together. 
        # By joining the left handside to the middle elements and finally the right-hand side.
        return quick_sort(less) + equal + quick_sort(greater)
 

# A test array.
an_array = [4, 32, 6, 0, 21, 16]
print(quick_sort(an_array)) # Calling the function and printing the output.