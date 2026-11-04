class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        result=[]
        def dfs(node, path):
            if not node:
                return
            path.append(chr(node.val+ord('a')))
            if not node.left and not node.right:
                result.append(''.join(reversed(path)))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return min(result)