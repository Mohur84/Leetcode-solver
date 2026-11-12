class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue=deque([root])
        max_sum=float('-inf')
        answer=1
        level=1
        while queue:
            level_sum=0
            for _ in range(len(queue)):
                node=queue.popleft()
                level_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum>max_sum:
                max_sum=level_sum
                answer=level
            level+=1
        return answer