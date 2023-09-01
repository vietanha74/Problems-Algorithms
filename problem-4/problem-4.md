### Aproach ###
To solve this problem, we can follow these steps:
1. The algorithm works by handling three pointers:
    - A low pointer points to the first 0 in the array.
    - A mid pointer scans the array from left to right.
    - A high pointer points to the last element in the array.
2. Loop until mid is greater than or equal to high. In each iteration of the loop:
    - If the value is 0, the function swaps the elements at indices low and mid => increments low and mid 1
    - If the value is 1, increments mid 1.
    - If the value is 2, the function swaps the elements at indices mid and high => decrements high 1

### Run time complexity ###
Run time complexity is O(n), where n is the number of elements in the array. Because the function iterates through the array once.
### Space complexity ###
Space complexity is O(1), where n is the number of elements in the array. This is because the function does not use any additional memory
