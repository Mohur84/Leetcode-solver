class Solution:
    def isNumber(self, s):
        s=s.strip()
        seenDigit=False
        seenDot=False
        seenExp=False
        digitAfterExp=True
        for i, ch in enumerate(s):
            if ch.isdigit():
                seenDigit=True
                digitAfterExp=True
            elif ch in ['+','-']:
                if i>0 and s[i-1] not in ['e','E']:
                    return False
            elif ch=='.':
                if seenDot or seenExp:
                    return False
                seenDot=True
            elif ch in ['e','E']:
                if seenExp or not seenDigit:
                    return False
                seenExp=True
                digitAfterExp=False
            else:
                return False
        return seenDigit and digitAfterExp
