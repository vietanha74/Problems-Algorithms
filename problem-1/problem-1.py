def sqrt(number):
    start = 0
    end = number
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            start = mid + 1
        else:
            end = mid - 1
    return end

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Fail" if (0 == sqrt(-9)) else "Pass")  # Edge case: negative number
print("Fail" if (3.25 == sqrt(3.25)) else "Pass")  # Edge case: decimal number
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

