from collections import deque
class Codec:
    def serialize(self, root):
        if not root:
            return ""
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                result.append("#")
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)
    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            current = q.popleft()
            if nodes[i] != "#":
                current.left = TreeNode(int(nodes[i]))
                q.append(current.left)
            i += 1
            if nodes[i] != "#":
                current.right = TreeNode(int(nodes[i]))
                q.append(current.right)
            i += 1
        return root