class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        freq=Counter()
        for word in words:
            mask=0
            for ch in word:
                mask |=1<<(ord(ch)-ord('a'))
            if mask.bit_count()<=7:
                freq[mask]+=1
        result=[]
        for puzzle in puzzles:
            first_bit=1<<(ord(puzzle[0])-ord('a'))
            mask=0
            for ch in puzzle[1:]:
                mask |=1<<(ord(ch)-ord('a'))
            count=0
            subset=mask
            while True:
                current_mask=subset | first_bit
                count+=freq[current_mask]
                if subset==0:
                    break
                subset=(subset-1) & mask
            result.append(count)
        return result