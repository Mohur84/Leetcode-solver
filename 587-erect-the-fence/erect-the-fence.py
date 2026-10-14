class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        trees=sorted(map(tuple, trees))
        if len(trees)<=3:
            return[list(p) for p in trees]
        def cross(o, a, b):
            return(
                (a[0]-o[0])*(b[1]-o[1])
                -(a[1]-o[1])*(b[0]-o[0])
            )
        lower=[]
        for p in trees:
            while len(lower)>=2 and cross(lower[-2], lower[-1], p)<0:
                lower.pop()
            lower.append(p)
        upper=[]
        for p in reversed(trees):
            while len(upper)>=2 and cross(upper[-2], upper[-1], p)<0:
                upper.pop()
            upper.append(p)
        hull=set(lower+upper)
        return[list(p) for p in hull]