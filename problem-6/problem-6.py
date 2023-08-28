def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    min_val = ints[0]
    max_val = ints[0]
    for element in ints[1:]:
        # Update min_val if the current element is smaller
        if element < min_val:
            min_val = element
        # Update max_val if the current element is larger
        if element > max_val:
            max_val = element

    # Return a tuple containing min_val and max_val
    return min_val, max_val        
    pass

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test cases
test_case_1 = [5, 2, 9, 1, 5, 6]
test_case_2 = [0, 0, 0, 0, 0]
test_case_3 = [10, -5, 20, 7, -15, 30]

# Finding minimum and maximum values for each test case
min_val_1, max_val_1 = get_min_max(test_case_1)
min_val_2, max_val_2 = get_min_max(test_case_2)
min_val_3, max_val_3 = get_min_max(test_case_3)

# Printing the results for each test case
print("Test Case 1 - Minimum value:", min_val_1, "Maximum value:", max_val_1)
print("Test Case 2 - Minimum value:", min_val_2, "Maximum value:", max_val_2)
print("Test Case 3 - Minimum value:", min_val_3, "Maximum value:", max_val_3)
