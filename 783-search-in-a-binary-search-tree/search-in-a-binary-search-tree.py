class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        while root:
            if root.val==val:
                return root
            elif val<root.val:
                root=root.left
            else:
                root=root.right
        return None