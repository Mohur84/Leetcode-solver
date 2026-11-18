class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        available=Counter(letters)
        n=len(words)
        def backtrack(index):
            if index==n:
                return 0
            best=backtrack(index+1)
            word_count=Counter(words[index])
            word_score=0
            possible=True
            for ch, count in word_count.items():
                if count>available[ch]:
                    possible=False
                    break
                word_score+=count*score[ord(ch)-ord('a')]
            if possible:
                for ch, count in word_count.items():
                    available[ch]-=count
                best=max(best, word_score+backtrack(index+1))
                for ch, count in word_count.items():
                    available[ch]+=count
            return best
        return backtrack(0)