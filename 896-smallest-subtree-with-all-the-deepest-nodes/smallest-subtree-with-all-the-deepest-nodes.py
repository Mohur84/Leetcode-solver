class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node):
            if not node:
                return 0, None
            left_depth, left_node=dfs(node.left)
            right_depth, right_node=dfs(node.right)
            if left_depth==right_depth:
                return left_depth+1, node
            if left_depth>right_depth:
                return left_depth+1, left_node
            return right_depth+1, right_node
        return dfs(root)[1]