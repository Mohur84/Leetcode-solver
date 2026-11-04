class Solution:
    def verticalTraversal(self, root):
        nodes = []
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        nodes.sort()
        result = []
        previous_col = None
        for col, row, value in nodes:
            if col != previous_col:
                result.append([])
                previous_col = col
            result[-1].append(value)
        return result