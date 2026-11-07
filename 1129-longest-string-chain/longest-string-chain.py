class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        dp={}
        answer=0
        for word in words:
            dp[word]=1
            for i in range(len(word)):
                predecessor=word[:i]+word[i+1:]
                if predecessor in dp:
                    dp[word]=max(
                        dp[word],
                        dp[predecessor]+1
                    )
            answer=max(answer, dp[word])
        return answer