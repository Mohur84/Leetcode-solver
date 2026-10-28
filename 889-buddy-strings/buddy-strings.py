class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        differences=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                differences.append(i)
        if len(differences)!=2:
            return False
        i, j=differences
        return s[i]==goal[j] and s[j]==goal[i]