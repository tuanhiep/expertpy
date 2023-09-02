def find_missing_number(nums):
    print("debug: " + str(nums))
    n = len(nums)
    i = 0
    while i < n:
        if 0 <= nums[i] < n and nums[i] != i and nums[i] != nums[nums[i]]:
            # Swap nums[i] with nums[nums[i]]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            print("debug: " + str(nums))
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    # If no missing number is found, return N
    return n


print("Test case 1")
result = find_missing_number([4, 0, 3, 1])
print("Missing number is: " + str(result))

print("Test case 2")
result = find_missing_number([3, 2, 2, 1])
print("Missing number is: " + str(result))


