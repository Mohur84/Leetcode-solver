class Solution:
    def pathSum(self, root, targetSum):
        prefix=defaultdict(int)
        prefix[0]=1
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum+=node.val
            count=prefix[current_sum-targetSum]
            prefix[current_sum]+=1
            count+=dfs(node.left, current_sum)
            count+=dfs(node.right, current_sum)
            prefix[current_sum]-=1
            return count
        return dfs(root, 0)