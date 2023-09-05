def minimizeSubsetSumDifference(nums):
    n = len(nums) // 2

    def calculate_min_subset_sum_diff(i, n, sum1, sum2, selected1, selected2):
        if i == 0:
            if n == 0:
                return abs(sum1 - sum2), selected1, selected2
            return float("inf"), None, None
        # Try including nums[i-1] in the first subset.
        if n > 0:
            diff1, sel1, sel2 = calculate_min_subset_sum_diff(i - 1, n - 1, sum1 + nums[i - 1], sum2,
                                                              selected1 + [nums[i - 1]],
                                                              selected2)

        # Try including nums[i-1] in the second subset.
        diff2, sel3, sel4 = calculate_min_subset_sum_diff(i - 1, n, sum1, sum2 + nums[i - 1],
                                                          selected1,
                                                          selected2 + [nums[i - 1]])
        if n == 0:
            return diff2, sel3, sel4
        if diff1 < diff2:
            return diff1, sel1, sel2
        else:
            return diff2, sel3, sel4

    min_diff, subset1, subset2 = calculate_min_subset_sum_diff(len(nums), n, 0, 0, [], [])

    return min_diff, subset1, subset2


# Test case 1:
nums = [3, 9, 7, 3]
result = minimizeSubsetSumDifference(nums)
print("Minimum Subset Sum Difference:", result)
# Test case 2:
nums = [2, -1, 0, 4, -2, -9]
result = minimizeSubsetSumDifference(nums)
print("Minimum Subset Sum Difference:", result)


