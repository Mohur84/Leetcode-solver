class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))
        a=b=-1
        result=0
        for start, end in intervals:
            if start>b:
                a, b=end-1, end
                result+=2
            elif start>a:
                a, b=b, end
                result+=1
        return result