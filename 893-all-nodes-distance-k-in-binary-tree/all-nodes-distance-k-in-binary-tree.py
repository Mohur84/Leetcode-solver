class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        def build_parent(node, par):
            if not node:
                return
            parent[node]=par
            build_parent(node.left, node)
            build_parent(node.right, node)
        build_parent(root, None)
        queue=deque([target])
        visited={target}
        distance=0
        while queue:
            if distance==k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                node=queue.popleft()
                for neighbor in(
                    node.left,
                    node.right,
                    parent[node]
                ):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance+=1
        return []