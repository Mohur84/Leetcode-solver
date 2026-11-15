class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x//gcd(x, y)*y
        ab=lcm(a, b)
        ac=lcm(a, c)
        bc=lcm(b, c)
        abc=lcm(ab, c)
        def count(x):
            return(
                x//a+x//b+x//c-x//ab-x//ac-x//bc+x//abc
            )
        left=1
        right=min(a, b, c)*n
        while left<right:
            mid=(left+right)//2
            if count(mid)>=n:
                right=mid
            else:
                left=mid+1
        return left