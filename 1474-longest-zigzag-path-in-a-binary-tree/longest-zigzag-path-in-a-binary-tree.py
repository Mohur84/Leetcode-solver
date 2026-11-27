class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        result=0
        def dfs(node):
            nonlocal result
            if node is None:
                return (-1, -1)
            left_child=dfs(node.left)
            right_child=dfs(node.right)
            left=left_child[1]+1
            right=right_child[0]+1
            result=max(result, left, right)
            return(left, right)
        dfs(root)
        return result