class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1, n+1):
            width=0
            height=0
            for j in range(i, 0, -1):
                book_width, book_height=books[j-1]
                width+=book_width
                if width>shelfWidth:
                    break
                height=max(height, book_height)
                dp[i]=min(dp[i], dp[j-1]+height)
        return dp[n]