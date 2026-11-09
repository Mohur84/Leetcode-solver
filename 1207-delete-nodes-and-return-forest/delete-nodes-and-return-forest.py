class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set=set(to_delete)
        forest=[]
        def dfs(node):
            if not node:
                return None
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            if node.val in delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node
        root=dfs(root)
        if root:
            forest.append(root)
        return forest