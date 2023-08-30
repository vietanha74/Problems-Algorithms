### Aproach ###
Declares two variables, min_val and max_val, to store the minimum and maximum values in the list. Then iterates over the list
For each element, the function checks if the element is smaller than the current minimum value => the minimum value is updated to the current element.
also checks if the element is larger than the current maximum value => the maximum value is updated to the current element.

### Run time complexity ###
The run time complexity of the function get_min_max() is O(n), where n is the number of elements in the list , because the function iterates over the entire list once, and each iteration takes constant time.
