class Solution:
    def sufficientSubset(self, root: TreeNode | None, limit: int) -> TreeNode | None:
        def dfs(node, current_sum):
            if not node:
                return None
            current_sum+=node.val
            if not node.left and not node.right:
                if current_sum<limit:
                    return None
                return node
            node.left=dfs(node.left, current_sum)
            node.right=dfs(node.right, current_sum)
            if not node.left and not node.right:
                return None
            return node
        return dfs(root, 0)