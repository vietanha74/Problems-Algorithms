### Aproach ###
To solve this problem, we can follow these steps:
 
1. Modify function rearrange_digits
    - Sort the input list in descending order using the mergesort_descending()
    - Initialize num1, num2 is 0
    - Iterate over the sorted list and distribute the digits alternately
        + If The even indices will be used to form the num1
        + If The even indices will be used to form the num2
    -  Returns the list [num1, num2].
2. Create mergesort_descending() function with 2 parameters : left, right as sorted arrays 
    - Creates an empty list merged. It then initializes two indices, left_index and right_index, to 0.
    - Iterates over the two sorted arrays left and right until one of the two arrays is exhausted
        + Compare element at the current indices of the two arrays. The element that is greater is appended to the merged list
    - returns the merged list.
3.  Create mergesort_descending 
    - Divides the array into two halves, left and right.
    - Recursively left and right using the mergesort_descending() function.
    - Return merge_descending() function with parameters is left and right

### Run time complexity ###
The number of steps required to sort a half of an array has size n is (n/2) log n so the total number required to sort an array of size n using the mergesort is : O(n log n)
### Space complexity ###
The space complexity of the mergesort algorithm is O(n). Because the mergesort is Stable algorithm.
