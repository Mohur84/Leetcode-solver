class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        MOD=10**9+7
        subtree_sums=[]
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            total=node.val+left+right
            subtree_sums.append(total)
            return total
        total_sum=dfs(root)
        max_product=0
        for sub_sum in subtree_sums:
            other_sum=total_sum-sub_sum
            product=sub_sum*other_sum
            max_product=max(max_product, product)
        return max_product%MOD