class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        n=len(arr)
        total=sum(arr)
        if total%3 !=0:
            return[-1, -1]
        if total==0:
            return[0, 2]
        ones_per_part=total//3
        first=second=third=-1
        count=0
        for i in range(n):
            if arr[i]==1:
                count+=1
                if count==1:
                    first=i
                elif count==ones_per_part+1:
                    second=i
                elif count==2*ones_per_part+1:
                    third=i
        while third<n:
            if arr[first]!=arr[second] or arr[second]!=arr[third]:
                return[-1, -1]
            first+=1
            second+=1
            third+=1
        return[first-1, second]