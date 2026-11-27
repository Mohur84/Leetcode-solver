class Solution:
    def maxSumBST(self, root):
        self.ans = 0
        def dfs(node):
            if not node:
                return (float('inf'), float('-inf'), 0)
            lmin, lmax, lsum = dfs(node.left)
            rmin, rmax, rsum = dfs(node.right)
            if lmax < node.val < rmin:
                total = lsum + rsum + node.val
                self.ans = max(self.ans, total)
                return (
                    min(lmin, node.val),
                    max(rmax, node.val),
                    total
                )
            return (float('-inf'), float('inf'), 0)
        dfs(root)
        return self.ans