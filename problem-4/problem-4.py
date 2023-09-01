def sort_012(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1
    
    while mid <= high:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

        #print(input_list)
        #print(mid,low,high)
        #print('------------------')

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([2, 0, 1, 1, 2, 0, 0, 1])  # Standard test case
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])  # Large test case

# Edge Cases
test_function([])  # Edge case: Empty list
test_function([1])  # Edge case: List with a single element [1]
test_function([0, 0, 0, 1, 1, 1, 2, 2, 2])  # Edge case: Already sorted list
test_function([2, 2, 2, 1, 1, 1, 0, 0, 0])  # Edge case: Reverse sorted list
