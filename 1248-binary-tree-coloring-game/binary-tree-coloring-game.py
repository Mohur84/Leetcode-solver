class Solution:
    def btreeGameWinningMove(self, root: TreeNode | None, n: int, x: int) -> bool:
        left_count=0
        right_count=0
        def count(node):
            nonlocal left_count, right_count
            if not node:
                return 0
            left=count(node.left)
            right=count(node.right)
            if node.val==x:
                left_count=left
                right_count=right
            return left+right+1
        count(root)
        parent_count=n-left_count-right_count-1
        largest_region=max(
            left_count,
            right_count,
            parent_count
        )
        return largest_region>n//2