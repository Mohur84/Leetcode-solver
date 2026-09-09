class Solution(object):
    def zigzagLevelOrder(self, root):
        result=[]
        if not root:
            return result
        q=deque([root])
        leftToRight=True
        while q:
            size=len(q)
            level=[0]*size
            for i in range(size):
                node=q.popleft()
                index=i if leftToRight else size-1-i
                level[index]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            leftToRight=not leftToRight
            result.append(level)
        return result        