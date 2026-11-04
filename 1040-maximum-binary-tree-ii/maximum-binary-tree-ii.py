class Solution:
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None or val>root.val:
            new_node=TreeNode(val)
            new_node.left=root
            return new_node
        root.right=self.insertIntoMaxTree(root.right, val)
        return root