class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        parent_count=[0]*n
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child!=-1:
                    parent_count[child]+=1
                    if parent_count[child]>1:
                        return False
        roots=[i for i in range(n) if parent_count[i]==0]
        if len(roots)!=1:
            return False
        root=roots[0]
        visited=set()
        stack=[root]
        while stack:
            node=stack.pop()
            if node in visited:
                return False
            visited.add(node)
            left=leftChild[node]
            right=rightChild[node]
            if left!=-1:
                stack.append(left)
            if right!=-1:
                stack.append(right)
        return len(visited)==n