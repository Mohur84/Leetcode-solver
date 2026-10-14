class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length=len(n)
        num=int(n)
        prefix_len=(length+1)//2
        prefix=int(n[:prefix_len])
        candidates={
            10**(length-1)-1,
            10**length+1
        }
        for p in (prefix-1, prefix, prefix+1):
            left=str(p)
            if length%2==0:
                palindrome=left+left[::-1]
            else:
                palindrome=left+left[:-1][::-1]
            candidates.add(int(palindrome))
        candidates.discard(num)
        answer=min(candidates, key=lambda x: (abs(x-num),x))
        return str(answer)