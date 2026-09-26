class Solution:
    def wordBreak(self, s, wordDict):
        wordSet=set(wordDict)
        memo={}
        def dfs(start):
            if start in memo:
                return memo[start]
            if start==len(s):
                return [""]
            res=[]
            for end in range(start+1, len(s)+1):
                word=s[start:end]
                if word in wordSet:
                    for suffix in dfs(end):
                        if suffix:
                            res.append(word+" "+suffix)
                        else:
                            res.append(word)
            memo[start]=res
            return res
        return dfs(0)
