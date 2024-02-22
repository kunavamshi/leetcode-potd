from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trusted_count = [0] * (n + 1)
        trusts_count = [0] * (n + 1)

        for a, b in trust:
            trusts_count[a] += 1
            trusted_count[b] += 1

        for i in range(1, n + 1):
            if trusts_count[i] == 0 and trusted_count[i] == n - 1:
                return i

        return -1

# Test cases
solution = Solution()
print(solution.findJudge(2, [[1,2]])) # Output: 2
print(solution.findJudge(3, [[1,3],[2,3]])) # Output: 3
print(solution.findJudge(3, [[1,3],[2,3],[3,1]])) # Output: -1