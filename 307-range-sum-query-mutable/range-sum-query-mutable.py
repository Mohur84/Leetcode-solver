class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self._add(i + 1, nums[i])
    def _add(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)
    def _prefix_sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total
    def sumRange(self, left, right):
        return self._prefix_sum(right + 1) - self._prefix_sum(left)