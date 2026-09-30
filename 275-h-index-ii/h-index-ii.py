class Solution:
    def hIndex(self, citations):
        n=len(citations)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            papers=n-mid
            if citations[mid]>=papers:
                right=mid-1
            else:
                left=mid+1
        return n-left