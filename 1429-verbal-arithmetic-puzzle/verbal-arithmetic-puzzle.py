class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        if len(set(''.join(words)+result))>10:
            return False
        max_len=max(map(len, words))
        if len(result)<max_len or len(result)>max_len+1:
            return False
        leading=set(word[0] for word in words + [result] if len(word)>1)
        mapping={}
        used=set()
        def solve(col, row, total):
            if col==len(result):
                return total==0
            if row==len(words):
                digit=total%10
                carry=total//10
                ch=result[-1-col]
                if ch in mapping:
                    if mapping[ch]!=digit:
                        return False
                    return solve(col+1, 0, carry)
                if digit in used:
                    return False
                if digit==0 and ch in leading:
                    return False
                mapping[ch]=digit
                used.add(digit)
                if solve(col+1, 0, carry):
                    return True
                del mapping[ch]
                used.remove(digit)
                return False
            word=words[row]
            if col>=len(word):
                return solve(col, row+1, total)
            ch=word[-1-col]
            if ch in mapping:
                return solve(col, row+1, total+mapping[ch])
            for digit in range(10):
                if digit in used:
                    continue
                if digit==0 and ch in leading:
                    continue
                mapping[ch]=digit
                used.add(digit)
                if solve(col, row+1, total+digit):
                    return True
                del mapping[ch]
                used.remove(digit)
            return False
        return solve(0, 0, 0)