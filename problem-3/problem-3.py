def rearrange_digits(input_list):
    result = []
    
    if len(input_list) == 0:
        return result

    # Sort the input list using merge sort
    sorted_list = merge_sort(input_list)

    num1 = 0
    num2 = 0

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1 = num1 * 10 + sorted_list[i]
        else:
            num2 = num2 * 10 + sorted_list[i]

    result.append(num1)
    result.append(num2)

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test case
test_function([[1, 2, 3, 4, 5], [531, 42]])
