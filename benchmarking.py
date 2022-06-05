#*********************** BENCHMARKING APPLICATION SCRIPT ***********************#


# Importing libraries. 
import time # For runtimes.
import numpy as np # For data manipulation.
import pandas as pd # For dataframes & data manipulation.
import matplotlib.pyplot as plt # For plotting/visualisation. 
import random # For random array generation.



#*********************** SORTING ALGORITHMS ***********************#

# The 5 selected sorting algorithms - Insertion Sort, Quick Sort, Counting Sort, Bubble Sort, Selection Sort.

# Insertion Sort Algorithm.
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


# QuickSort Algorithm.
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


# Counting Sort Algorithm.
# Defining the function.
def counting_sort(array):
     # An array to store the frequency each unique element appears.
     # Getting the biggest element in the array + 1. E.g., if it was 5 it would be 6.
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
        # Overwrite the original input with the elements correct position. Decrease by -1 (we +1 earlier).
        sorted[count[element] - 1] = element
    # Return sorted array.
    return sorted


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



# Selection Sort Algorithm.
# Defining the function.
def selection_sort(array):
    # Outer loop which runs the length of the passed array.
    for element in range(len(array) - 1): 
        # Variable to store the minimum element.
        min_value = element
        # Inner loop which compares the leftmost value to the other values on the right-hand side.
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




#*********************** BENCHMARKING APPLICATION ***********************#


# Defining the benchmarking application.
# Which takes in an algorithm, input size (n) & number times to run. 
def benchmarking(algorithms, n, runs):
    print("Now running benchmarking application...\n")


    # Empty arrays to store the output. Which will be used to create a dataframe.
    algorithm_name = [] # The algorithm selected.
    input_size = [] # For the input size (n).
    run_number = [] # To keep count of the run number (1-10).
    running_times = [] # For the running time of each run.
   
    
    # For each algorithm. 
    for al in algorithms:
        print('Please wait while we load and run: ' + al.upper() + ' ■■■■■■■■■■■□□□...') # Print.       
        # For each of the passed input sizes (n).
        for size in n:
            # For each of the input size run this loop the number of times passed (10).
            for run in range(runs):
                # Generates random arrays between 0-100 for the given input size (n).
                random_array = [random.randint(0,101) for i in range(size)]
                # Test for myself to make sure each run/algorithm had a different random array.
                # print(random_array)
                # Variable for the algorithm in use.
                algorithm = algorithms[al]
                # Variable to keep track of the start time. 
                # .time() returns number of seconds passed since epoch i.e. starting point used to calculate the number of seconds elapsed.
                start_time = time.time() * 1000 # Project specification asked for time to be in milliseconds - x 1000.
                # Calling the algorithm (see line 19-140) on the generated arrays.
                algorithm(random_array)
                # Variable  to keep track of the end time also since epoch.
                end_time = time.time() * 1000  # Project specification asked for time to be in milliseconds - x 1000.
                # To get the runtime end - start time.
                runtime = (end_time - start_time)
          
               
                # Add results to previously created empty arrays.
                running_times.append(runtime)  # Add the runtime to empty array.           
                run_number.append(run + 1)     # Add run number to empty array, increase by 1 each time.
                input_size.append(size)        # Add input size (n) to empty array.
                algorithm_name.append(al)      # Add algorithm to empty array. 
       
        

    #*********************** DATAFRAME ***********************#    

    # Print a new line.     
    print('\n')    
    # Creating a pandas dataframe from the populated arrays to tidy the output.
    # Also, will allow for graph generation as requested in project specification.
    # df = pd.DataFrame[algorithm_name, run_number, input_size, running_times]
    # df.columns = ['Algorithm', 'Input Size (n)', "Runtime", "Run #"]
    
    # Above wasn't working found https://www.educative.io/courses/data-analysis-processing-with-pandas/q2pYRjnxlGR suggested using a dictionary of lists.
    # Creating a pandas dataframe using a dictionary of lists with results for each run.          
    df = pd.DataFrame({'Algorithm': algorithm_name, 'Input Size (n)': input_size, 'Runtime':running_times, 'Run #': run_number})
    #print(df) 
    
    # Selecting an index. Using the same index as the project output example.
    df.set_index('Input Size (n)', inplace=True) # Modified inplace.
    # Project specification asked that running time output is the average of 10 runs to 3 decimal places.
    # Using pandas .iloc to select rows/columns - Algorithm, Input Size (n), Runtime.
    # Grouping the Algorithm, Input Size (n) columns so .mean() can be applied.
    average = (df.iloc[:, :2].groupby(['Algorithm','Input Size (n)']).mean().round(3))
   
    #print(average) # Checking current dataframe.

    # Cleaning up dataframe for output. 
    # Reassigning the dataframe.
    df = average.unstack()  # Current dataframe is stacked i.e., has a multilevel index. To match example we use .unstack().
    df.rename_axis(None, inplace=True)  # Removing the 'Algorithm' headinig. 
    df.columns = df.columns.droplevel() # Dropping 'Runtime' level https://www.w3resource.com/pandas/series/series-droplevel.php.


    # Printing final console output.
    print('##########################################################################################################')
    print(df)
    print('##########################################################################################################')

   


    #*********************** PLOTTING ***********************#

    plt.rcParams['figure.figsize'] = (15, 10)           # Standard plot size.
    plt.style.use('fivethirtyeight')                    # Selecting plot style.
    df.T.plot(lw=2.5, marker='s')                       # Plotting the data. .T transposes index and columns of the dataframe.
    plt.title('Average Runtime of Sorting Algorithms')  # Adding  title.
    plt.ylabel("Running Time (milliseconds)")           # Labelling y-axis.
    plt.xlabel("Input Size")                            # Labelling x-axis.
    plt.legend(loc='best')                              # Adding a legend to best posistion.                        
    plt.grid(c='black', ls='--', alpha=0.5)             # Adding a grid.
    plt.savefig('benchmarking_results_plot.png')        # Saving the plot.
    




#*********************** MAIN PROGRAMME ***********************#

# Calling main programme.
if __name__ == "__main__":

    # Dictionary to store reference to the different sorting algorithm functions to be used. 
    algorithms = {"Bubble Sort": bubble_sort, "Counting Sort": counting_sort, "Insertion Sort": insertion_sort, "Quick Sort": quick_sort, "Selection Sort": selection_sort}

    # Small input (n) sizes to quickly test benchmarking() is working.  
    #input_n = [5, 10, 15, 20, 30, 40, 50, 60, 70, 80]
    # Array of input sizes (n) to be used.
    input_n = [50, 100, 250, 750, 1000, 2000, 3500, 5250, 8500, 10000]
 
    # Calling the function. Passing the algorithm, input size (n) and how many times to run.
    benchmarking(algorithms, input_n, 10)
   
  

   
   


