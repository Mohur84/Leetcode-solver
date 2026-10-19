class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        minimum=root.val
        second=float('inf')
        def dfs(node):
            nonlocal second
            if not node:
                return
            if minimum<node.val<second:
                second=node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return second if second!=float('inf') else -1