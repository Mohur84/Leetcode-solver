class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        topLeft=self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight=self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft=self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight=self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        children=[topLeft, topRight, bottomLeft, bottomRight]
        if all(child.isLeaf for child in children):
            if all(child.val==children[0].val for child in children):
                return Node(children[0].val, True, None, None, None, None)
        return Node(
            False, False,
            topLeft, topRight, bottomLeft, bottomRight
        )            