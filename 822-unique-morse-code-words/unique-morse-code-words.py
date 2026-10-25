class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse=[
            ".-","-...","-.-.","-..",".","..-.",
            "--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-",
            "-.--","--.."
        ]
        transformations=set()
        for word in words:
            code="".join(morse[ord(ch)-ord('a')] for ch in word)
            transformations.add(code)
        return len(transformations)