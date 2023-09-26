class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Size of the tree is typically 4 times the size of the array
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, tree_index, start, end):
        if start == end:
            self.tree[tree_index] = arr[start]
        else:
            mid = (start + end) // 2
            left_index = 2 * tree_index + 1
            right_index = 2 * tree_index + 2
            self.build(arr, left_index, start, mid)
            self.build(arr, right_index, mid + 1, end)
            self.tree[tree_index] = self.tree[left_index] + self.tree[right_index]

    def query(self, tree_index, start, end, query_start, query_end):
        if start > query_end or end < query_start:
            return 0
        if start >= query_start and end <= query_end:
            return self.tree[tree_index]

        mid = (start + end) // 2
        left_index = 2 * tree_index + 1
        right_index = 2 * tree_index + 2
        left_sum = self.query(left_index, start, mid, query_start, query_end)
        right_sum = self.query(right_index, mid + 1, end, query_start, query_end)
        return left_sum + right_sum

    def range_query(self, query_start, query_end):
        return self.query(0, 0, self.n - 1, query_start, query_end)

    def update(self, tree_index, start, end, index, new_value):
        if start == end:
            self.tree[tree_index] = new_value
        else:
            mid = (start + end) // 2
            left_index = 2 * tree_index + 1
            right_index = 2 * tree_index + 2
            if index <= mid:
                self.update(left_index, start, mid, index, new_value)
            else:
                self.update(right_index, mid + 1, end, index, new_value)
            self.tree[tree_index] = self.tree[left_index] + self.tree[right_index]


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Query the sum of elements in range [2, 4]:
print(seg_tree.range_query(2, 4))  # Output: 21 (5 + 7 + 9)

# Update the element at index 3 to 6:
seg_tree.update(0, 0, len(arr) - 1, 3, 6)

# Query the sum of elements in range [2, 4] after the update:
print(seg_tree.range_query(2, 4))  # Output: 20 (5 + 6 + 9)
