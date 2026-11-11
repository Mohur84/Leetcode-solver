class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = ""
        right = ""
        result = 0
        i = 0
        j = len(text) - 1
        while i <= j:
            left += text[i]
            right = text[j] + right
            if left == right:
                if i == j:
                    result += 1
                else:
                    result += 2
                left = ""
                right = ""
            i += 1
            j -= 1
        if left:
            result += 1
        return result