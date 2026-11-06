class StreamChecker:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
    def __init__(self, words):
        self.root = self.TrieNode()
        self.stream = []
        self.max_len = max(len(word) for word in words)
        for word in words:
            node = self.root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = self.TrieNode()
                node = node.children[ch]
            node.is_end = True
    def query(self, letter):
        self.stream.append(letter)
        node = self.root
        for ch in reversed(self.stream[-self.max_len:]):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end:
                return True
        return False