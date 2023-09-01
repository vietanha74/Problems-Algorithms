## Find the index by searching in a rotated sorted array ##

### Aproach ###
I implement how to implement searching in a rotated sorted array
1. Determine start value and end value .
2. Use while loop to perform binary search. In each iteration we find middle "mid" element. 
3. Compare input_list[mid] with "number"
    - if input_list[mid] == "number" => we found out and return the index of "mid"
    - if input_list[mid] is not "number" => we check search range from "start" to "mid" or "mid" to end" has sorted in decreasing segment.
    - If the range from start to mid or from mid to end is not sorted in a non-decreasing segment, we know that the array has been rotated in this segment, and we continue searching in the remaining range.
4. We keep repeating the process until find a number.
### Run time complexity ###
1. Since the number of iterations in the while loop is O(log(n)) and all other operations have O(1) time complexity, the time complexity of the sqrt function is O(log(n)) .
=> All operations take O(log(n))  
### Space complexity ###
Variable start, end, and mid are integer variables, which use constant space.
Input_list, and the results list has pace complexity is O(n) where is the length of input_list.
=> Overall, the space complexity of rotated_array_search is O(N) due to the input array
