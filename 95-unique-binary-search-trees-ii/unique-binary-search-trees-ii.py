class Solution:
    def generateTrees(self, n):
        if n==0:
            return []
        memo={}
        def build(start, end):
            if start>end:
                return[None]
            if(start, end) in memo:
                return memo[(start, end)]
            trees=[]
            for rootVal in range(start, end+1):
                leftTrees=build(start, rootVal-1)
                rightTrees=build(rootVal+1, end)
                for left in leftTrees:
                    for right in rightTrees:
                        root=TreeNode(rootVal)
                        root.left=left
                        root.right=right
                        trees.append(root)
            memo[(start, end)]=trees
            return trees
        return build(1, n)