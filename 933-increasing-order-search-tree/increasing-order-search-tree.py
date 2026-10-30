class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        dummy=TreeNode(0)
        current=dummy
        def inorder(node):
            nonlocal current
            if not node:
                return
            inorder(node.left)
            node.left=None
            current.right=node
            current=node
            inorder(node.right)
        inorder(root)
        return dummy.right