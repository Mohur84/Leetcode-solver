class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq=Counter(text)
        result=0
        for ch in freq:
            left=0
            count=0
            for right in range(len(text)):
                if text[right]==ch:
                    count+=1
                while(right-left+1)-count>1:
                    if text[left]==ch:
                        count-=1
                    left+=1
                window_length=right-left+1
                result=max(
                    result,
                    min(window_length, freq[ch])
                )
        return result