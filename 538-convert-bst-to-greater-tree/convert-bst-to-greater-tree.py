class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=0
        def reverse_inorder(node):
            nonlocal total
            if not node:
                return
            reverse_inorder(node.right)
            total+=node.val
            node.val=total
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root