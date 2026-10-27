class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def most_overlap_word(lst):
            cnts = [[0] * 26 for _ in range(6)]
            for word in lst:
                for i, c in enumerate(word):
                    cnts[i][ord(c) - ord('a')] += 1
            best_word, best_overlap = "", -1
            for word in lst:
                overlap = 0
                for i, c in enumerate(word):
                    overlap += cnts[i][ord(c) - ord('a')]
                if overlap > best_overlap:
                    best_word = word
                    best_overlap = overlap
            return best_word
        def pair_matches(w1, w2):
            cnt = 0
            for i in range(6):
                if w1[i] == w2[i]:
                    cnt += 1
            return cnt
        candidates = words[:]
        while candidates:
            guess_word = most_overlap_word(candidates)
            correct = master.guess(guess_word)
            if correct == 6:
                return
            candidates = [w for w in candidates if pair_matches(guess_word, w) == correct]