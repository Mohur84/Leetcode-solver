class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt=0
        def dfs(node):
            nonlocal total_tilt
            if not node:
                return 0
            left_sum=dfs(node.left)
            right_sum=dfs(node.right)
            total_tilt+=abs(left_sum-right_sum)
            return node.val+left_sum+right_sum
        dfs(root)
        return total_tilt