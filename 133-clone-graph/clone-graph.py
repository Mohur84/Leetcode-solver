class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        clones={}
        def dfs(curr):
            if curr in clones:
                return clones[curr]
            copy=Node(curr.val)
            clones[curr]=copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)