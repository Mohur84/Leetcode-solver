class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i=0
        j=0
        result=[]
        while i<len(firstList) and j<len(secondList):
            start=max(firstList[i][0], secondList[j][0])
            end=min(firstList[i][1], secondList[j][1])
            if start<=end:
                result.append([start, end])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return result