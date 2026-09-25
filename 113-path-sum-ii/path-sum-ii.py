class Solution:
    def pathSum(self, root, targetSum):
        ans=[]
        def dfs(node, remaining, path):
            if not node:
                return
            path.append(node.val)
            remaining-=node.val
            if not node.left and not node.right and remaining==0:
                ans.append(path[:])
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)
            path.pop()
        dfs(root, targetSum, [])
        return ans