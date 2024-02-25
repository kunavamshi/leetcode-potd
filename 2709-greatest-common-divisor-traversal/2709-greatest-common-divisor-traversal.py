from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        g = [[] for _ in range(n)]

        MAX = max(nums) + 1
        pos = [[] for _ in range(MAX)]

        for i in range(n):
            pos[nums[i]].append(i)

        for i in range(2, MAX):
            cur = []
            for j in range(i, MAX, i):
                cur.extend(pos[j])

            for j in range(1, len(cur)):
                g[cur[j]].append(cur[j - 1])
                g[cur[j - 1]].append(cur[j])

        vis = [False] * n
        cc = 0

        def dfs(node):
            nonlocal vis
            vis[node] = True
            for child in g[node]:
                if not vis[child]:
                    dfs(child)

        for i in range(n):
            if not vis[i]:
                cc += 1
                dfs(i)

        return cc == 1

# Example usage:
solution = Solution()
print(solution.canTraverseAllPairs([2, 3, 6]))  # Output: True
print(solution.canTraverseAllPairs([3, 9, 5]))  # Output: False
print(solution.canTraverseAllPairs([4, 3, 12, 8]))  # Output: True