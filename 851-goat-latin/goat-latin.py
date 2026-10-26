class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels=set("aeiouAEIOU")
        words=sentence.split()
        result=[]
        for i, word in enumerate(words, start=1):
            if word[0] not in vowels:
                word=word[1:]+word[0]
            word+="ma"+"a"*i
            result.append(word)
        return " ".join(result)