class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num=int(n)
        max_length=num.bit_length()
        for length in range(max_length, 1, -1):
            left=2
            right=int(num**(1/(length-1)))+1
            while left<=right:
                base=(left+right)//2
                total=1
                for _ in range(length-1):
                    total=total*base+1
                    if total>num:
                        break
                if total==num:
                    return str(base)
                elif total<num:
                    left=base+1
                else:
                    right=base-1
        return str(num-1)