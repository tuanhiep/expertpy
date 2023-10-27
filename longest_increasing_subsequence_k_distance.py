from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        def printSequence(nums, sequence, maxIdx):
            subsequence = []
            idx = maxIdx
            while sequence[idx] != -1:
                subsequence.append(nums[idx])
                idx = sequence[idx]
            print(subsequence[::-1])

        n = len(nums)
        # Initialize a dynamic programming table to store the lengths of longest subsequences.
        dp = [1] * n
        sequence = [-1] * n
        maxIdx = 0
        # Iterate through the elements in the sorted array.
        for i in range(1, n):
            for j in range(i):
                if nums[i] - nums[j] <= k and nums[i] > nums[j]:
                    # dp[i] = max(dp[i], dp[j] + 1)
                    if dp[j] + 1 > dp[i]:
                        sequence[i] = j
                        dp[i] = dp[j] + 1
                    if dp[i] > dp[maxIdx]:
                        maxIdx = i

        printSequence(nums, sequence, maxIdx)
        # The maximum value in the dp array is the length of the longest subsequence.
        return max(dp)
