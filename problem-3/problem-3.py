def mergesort_descending(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort_descending(left)
    right = mergesort_descending(right)
    
    return merge_descending(left, right)

def merge_descending(left,right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged

def rearrange_digits(input_list):
    # Sort the array in descending order
    input_list = mergesort_descending(input_list)

    # Initialize the two numbers
    num1 = 0
    num2 = 0

    # Iterate over the sorted array and form the two numbers
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 = num1 * 10 + input_list[i]
        else:
            num2 = num2 * 10 + input_list[i]

    return [num1, num2]

# Test cases
print(rearrange_digits([]))  # Edge case: Empty list
print(rearrange_digits([42]))  # Edge case: Single-element list
print(rearrange_digits([0, 0, 0, 0]))  # Edge case: List with repeated zeros
