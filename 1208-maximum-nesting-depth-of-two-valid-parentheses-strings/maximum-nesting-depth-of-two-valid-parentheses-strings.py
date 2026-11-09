class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result=[]
        depth=0
        for ch in seq:
            if ch=='(':
                depth+=1
                result.append(depth%2)
            else:
                result.append(depth%2)
                depth-=1
        return result