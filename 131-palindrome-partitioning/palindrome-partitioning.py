class Solution:
    def partition(self, s):
        ans=[]
        path=[]
        def isPalindrome(left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        def backtrack(start):
            if start==len(s):
                ans.append(path[:])
                return
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return ans