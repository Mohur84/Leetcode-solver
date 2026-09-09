class Solution(object):
    def maxPathSum(self, root):
        self.max_sum=float('-inf')
        self.dfs(root)
        return self.max_sum
    def dfs(self, node):
        if not node:
            return 0
        left=max(0, self.dfs(node.left))
        right=max(0, self.dfs(node.right))
        self.max_sum=max(
            self.max_sum,
            left+right+node.val
        )
        return max(left, right)+node.val
