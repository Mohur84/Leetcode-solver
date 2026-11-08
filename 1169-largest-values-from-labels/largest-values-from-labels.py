class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        items=sorted(zip(values, labels), reverse=True)
        count=defaultdict(int)
        total=0
        selected=0
        for value, label in items:
            if selected==numWanted:
                break
            if count[label]<useLimit:
                total+=value
                count[label]+=1
                selected+=1
        return total