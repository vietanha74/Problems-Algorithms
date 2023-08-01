## Square Root of an Integer ##

### Aproach ###
I implement how to finding the Square Root of an Integer
1. Step 1 : Determine the search range 
    - The search range from 1 to number // 2
2. Step 2 : Use Binary search to find number
    - In each iteration of binary search , we compute the value of square root at middle value and compare with the number.

### Run time complexity ###
1. Since the number of iterations in the while loop is O(log(n)) and all other operations have O(1) time complexity, the time complexity of the sqrt function is O(log(n)) .
=> All operations take O(log(n))  

