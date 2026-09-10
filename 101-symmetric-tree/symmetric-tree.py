class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        return isMirror(root.left, root.right) if root else True