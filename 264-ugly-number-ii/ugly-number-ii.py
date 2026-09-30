class Solution:
    def nthUglyNumber(self, n):
        ugly=[1]*n
        i2=0
        i3=0
        i5=0
        for i in range(1, n):
            next_num=min(
                ugly[i2]*2,
                ugly[i3]*3,
                ugly[i5]*5
            )
            ugly[i]=next_num
            if next_num==ugly[i2]*2:
                i2+=1
            if next_num==ugly[i3]*3:
                i3+=1
            if next_num==ugly[i5]*5:
                i5+=1
        return ugly[n-1]