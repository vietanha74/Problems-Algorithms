### Aproach ###
To solve this problem, we can follow these steps:
1. Declares two variables, min_val store minimun value and max_val store maximun value in the list
2. Iterates over the list of integers. For each element in the list:
    -  Checks if the element is smaller than the current value of min_val => update min_val
    -  Checks if the element is greater than the current value of max_val => update max_val
3. Finally returns a tuple containing the values of min_val and max_val.

### Run time complexity ###
The run time complexity of the function get_min_max() is O(n), where n is the number of elements in the list , because the function iterates over the entire list once, and each iteration takes constant time.

### Space complexity ###
In this function only uses two variables, which means that the space complexity is O(1).
