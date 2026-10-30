class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L=int(left)
        R=int(right)
        def is_palindrome(x):
            s=str(x)
            return s==s[::-1]
        count=0
        for seed in range(1, 100000):
            s=str(seed)
            odd_root=int(s+s[-2::-1])
            even_root=int(s+s[::-1])
            for root in (odd_root, even_root):
                square=root*root
                if square>R:
                    continue
                if square>=L and is_palindrome(square):
                    count+=1
        return count