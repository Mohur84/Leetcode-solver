class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isSameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val!=b.val:
                return False
            return(
                isSameTree(a.left, b.left)
                and isSameTree(a.right, b.right)
            )
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return(
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )