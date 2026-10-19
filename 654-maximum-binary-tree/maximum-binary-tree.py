class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        max_index=nums.index(max(nums))
        root=TreeNode(nums[max_index])
        root.left=self.constructMaximumBinaryTree(nums[:max_index])
        root.right=self.constructMaximumBinaryTree(nums[max_index+1:])
        return root        