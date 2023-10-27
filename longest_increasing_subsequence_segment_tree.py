from typing import List


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 4 * self.n

    def query(self, left, right, index, qleft, qright):
        if qright < left or qleft > right:
            return 0

        if qleft <= left and right <= qright:
            return self.tree[index]

        mid = (left + right) // 2
        resLeft = self.query(left, mid, 2 * index + 1, qleft, qright)
        resRight = self.query(mid + 1, right, 2 * index + 2, qleft, qright)
        return max(resLeft, resRight)

    def update(self, left, right, index, pos, val):
        if left == right:
            self.tree[index] = val
            return

        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2 * index + 1, pos, val)
        else:
            self.update(mid + 1, right, 2 * index + 2, pos, val)
        self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        segmentTree = SegmentTree(mx + 1)
        for num in nums:
            subLongest = segmentTree.query(0, segmentTree.n - 1, 0, num - k, num - 1) + 1
            segmentTree.update(0, segmentTree.n - 1, 0, num, subLongest)
        return segmentTree.tree[0]
