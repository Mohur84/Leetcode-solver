class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        cameras=0
        def dfs(node):
            nonlocal cameras
            if not node:
                return 2
            left=dfs(node.left)
            right=dfs(node.right)
            if left==0 or right==0:
                cameras+=1
                return 1
            if left==1 or right==1:
                return 2
            return 0
        if dfs(root)==0:
            cameras+=1
        return cameras