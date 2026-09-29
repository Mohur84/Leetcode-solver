class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None
class Solution:
    def findWords(self, board, words):
        root=TrieNode()
        for word in words:
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                node=node.children[ch]
            node.word=word
        rows=len(board)
        cols=len(board[0])
        result=[]
        def dfs(r, c, node):
            ch=board[r][c]
            if ch not in node.children:
                return
            next_node=node.children[ch]
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word=None
            board[r][c]='#'
            if r>0 and board[r-1][c]!='#':
                dfs(r-1, c, next_node)
            if r<rows-1 and board[r+1][c]!='#':
                dfs(r+1, c, next_node)
            if c>0 and board[r][c-1]!='#':
                dfs(r, c-1, next_node)
            if c<cols-1 and board[r][c+1]!='#':
                dfs(r, c+1, next_node)
            board[r][c]=ch
            if not next_node.children and next_node.word is None:
                del node.children[ch]
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result