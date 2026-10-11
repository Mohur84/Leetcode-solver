class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        freq=Counter()
        def dfs(node):
            if not node:
                return 0
            left_sum=dfs(node.left)
            right_sum=dfs(node.right)
            subtree_sum=node.val+left_sum+right_sum
            freq[subtree_sum]+=1
            return subtree_sum
        dfs(root)
        max_freq=max(freq.values())
        return[s for s, count in freq.items() if count==max_freq]