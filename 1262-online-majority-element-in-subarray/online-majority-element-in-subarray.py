from collections import defaultdict
from bisect import bisect_left
class MajorityChecker:
    def __init__(self, arr):
        self.n = len(arr)
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)
        self.tree = [(0, 0)] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)
    def merge(self, a, b):
        if a[1] == 0:
            return b
        if b[1] == 0:
            return a
        if a[0] == b[0]:
            return (a[0], a[1] + b[1])
        if a[1] > b[1]:
            return (a[0], a[1] - b[1])
        return (b[0], b[1] - a[1])
    def build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = (arr[start], 1)
            return
        mid = (start + end) // 2
        self.build(node * 2, start, mid, arr)
        self.build(node * 2 + 1, mid + 1, end, arr)
        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )
    def query_tree(self, node, start, end, left, right):
        if right < start or end < left:
            return (0, 0)
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        a = self.query_tree(
            node * 2, start, mid, left, right
        )
        b = self.query_tree(
            node * 2 + 1, mid + 1, end, left, right
        )
        return self.merge(a, b)
    def query(self, left, right, threshold):
        candidate, _ = self.query_tree(
            1, 0, self.n - 1, left, right
        )
        positions = self.positions[candidate]
        count = (
            bisect_left(positions, right + 1)
            - bisect_left(positions, left)
        )
        return candidate if count >= threshold else -1