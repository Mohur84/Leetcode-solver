class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        longest=0
        def dfs(node):
            nonlocal longest
            if not node:
                return 0
            left_length=dfs(node.left)
            right_length=dfs(node.right)
            left_path=0
            right_path=0
            if node.left and node.left.val==node.val:
                left_path=left_length+1
            if node.right and node.right.val==node.val:
                right_path=right_length+1
            longest=max(longest, left_path+right_path)
            return max(left_path, right_path)
        dfs(root)
        return longest