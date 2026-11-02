from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
        for r, c in stones:
            union(r, ~c)
        components = len({find(r) for r, c in stones})
        return len(stones) - components