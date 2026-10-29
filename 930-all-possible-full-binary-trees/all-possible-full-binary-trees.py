class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        @lru_cache(None)
        def build(nodes):
            if nodes==1:
                return(TreeNode(0),)
            trees=[]
            for left_nodes in range(1, nodes, 2):
                right_nodes=nodes-1-left_nodes
                if right_nodes<1:
                    continue
                left_trees=build(left_nodes)
                right_trees=build(right_nodes)
                for left in left_trees:
                    for right in right_trees:
                        trees.append(
                            TreeNode(0, left, right)
                        )
            return tuple(trees)
        if n%2==0:
            return[]
        return list(build(n))