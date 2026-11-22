class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        total=0
        def dfs(node, parent, grandparent):
            nonlocal total
            if not node:
                return
            if grandparent and grandparent.val%2==0:
                total+=node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        dfs(root, None, None)
        return total