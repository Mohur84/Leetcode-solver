class Solution:
    def __init__(self, rects: list[list[int]]):
        self.rects=rects
        self.prefix=[]
        total=0
        for x1, y1, x2, y2 in rects:
            points=(x2-x1+1)*(y2-y1+1)
            total+=points
            self.prefix.append(total)
        self.total=total
    def pick(self) -> list[int]:
        k=random.randint(1, self.total)
        idx=bisect_left(self.prefix, k)
        x1, y1, x2, y2 =self.rects[idx]
        width=x2-x1+1
        offset=k-(self.prefix[idx-1] if idx>0 else 0)-1
        x=x1+offset%width
        y=y1+offset//width
        return[x, y]