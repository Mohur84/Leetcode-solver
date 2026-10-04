class Solution:
    def rob(self, root: TreeNode):
        def dfs(node):
            if not node:
                return(0, 0)
            left_rob, left_skip=dfs(node.left)
            right_rob, right_skip=dfs(node.right)
            rob=node.val+left_skip+right_skip
            skip=max(left_rob, left_skip)+ \
                 max(right_rob, right_skip)
            return(rob, skip)
        rob_root, skip_root=dfs(root)
        return max(rob_root, skip_root)