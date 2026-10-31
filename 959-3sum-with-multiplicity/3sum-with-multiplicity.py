class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD=10**9+7
        count=[0]*101
        for num in arr:
            count[num]+=1
        result=0
        for i in range(101):
            for j in range(i, 101):
                k=target-i-j
                if k<j or k>100:
                    continue
                if i==j==k:
                    result+=(
                        count[i]*(count[i]-1)*
                        (count[i]-2)//6
                    )
                elif i==j:
                    result+=(
                        count[i]*(count[i]-1)//2
                    )*count[k]
                elif j==k:
                    result+=count[i]*(
                        count[j]*(count[j]-1)//2
                    )
                else:
                    result+=count[i]*count[j]*count[k]
                result%=MOD
        return result