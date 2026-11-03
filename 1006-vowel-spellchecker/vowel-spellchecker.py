class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        vowels=set("aeiou")
        def devowel(word):
            return ''.join(
                '*' if ch in vowels else ch
                for ch in word.lower()
            )
        exact=set(wordlist)
        case_map={}
        vowel_map={}
        for word in wordlist:
            lower=word.lower()
            if lower not in case_map:
                case_map[lower]=word
            pattern=devowel(word)
            if pattern not in vowel_map:
                vowel_map[pattern]=word
        result=[]
        for query in queries:
            if query in exact:
                result.append(query)
            elif query.lower() in case_map:
                result.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:
                result.append(vowel_map[devowel(query)])
            else:
                result.append("")
        return result