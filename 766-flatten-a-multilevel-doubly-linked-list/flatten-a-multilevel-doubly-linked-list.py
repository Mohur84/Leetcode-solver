class Solution:
    def flatten(self, head):
        if not head:
            return None
        stack=[head]
        prev=None
        while stack:
            node=stack.pop()
            if prev:
                prev.next=node
                node.prev=prev
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child=None
            prev=node
        return head