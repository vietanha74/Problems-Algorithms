### Aproach ###
The algorithm works by handling three pointers:
 + A low pointer points to the first 0 in the array.
 + A mid pointer scans the array from left to right.
 + A high pointer points to the last element in the array.

The algorithm works by repeat swapping the elements at the mid pointer with the element at the low pointer (if the element at the mid pointer is 0) or the element at the high pointer (if the element at the mid pointer is 2).

### Run time complexity ###
The run time complexity of the algorithm is O(n), which means that it takes time proportional to the size of the input. This is because the algorithm scans the entire array once, regardless of the size of the array.
