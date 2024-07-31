class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # dp[i] will store the minimum height for the first i books
        dp = [0] * (len(books) + 1)
        
        # Start filling the dp array
        for i in range(1, len(books) + 1):
            total_width = 0
            max_height = 0
            dp[i] = float('inf')
            # Place books[i-1] on the current shelf
            for j in range(i, 0, -1):
                total_width += books[j-1][0]
                if total_width > shelfWidth:
                    break
                max_height = max(max_height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + max_height)
        
        return dp[len(books)]