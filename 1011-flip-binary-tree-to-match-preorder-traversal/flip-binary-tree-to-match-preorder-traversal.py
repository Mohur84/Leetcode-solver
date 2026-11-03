class Solution:
    def flipMatchVoyage(self, root: TreeNode | None, voyage: list[int]) -> list[int]:
        flips=[]
        index=0
        def dfs(node):
            nonlocal index
            if not node:
                return True
            if index>=len(voyage) or node.val!=voyage[index]:
                return False
            index+=1
            if node.left and index<len(voyage) and node.left.val!=voyage[index]:
                flips.append(node.val)
                return dfs(node.right) and dfs(node.left)
            return dfs(node.left) and dfs(node.right)
        if not dfs(root):
            return[-1]
        return flips