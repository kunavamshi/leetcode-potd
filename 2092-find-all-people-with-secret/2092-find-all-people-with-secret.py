from typing import List, Tuple
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = [float('inf')] * (n + 1)
        ans[0] = 0
        ans[firstPerson] = 0

        g = [[] for _ in range(n + 1)]

        for i in meetings:
            g[i[0]].append((i[1], i[2]))
            g[i[1]].append((i[0], i[2]))

        pq = [(0, firstPerson), (0, 0)]

        while pq:
            time, node = heapq.heappop(pq)

            for next_node, next_time in g[node]:
                if next_time >= time and ans[next_node] > next_time:
                    ans[next_node] = next_time
                    heapq.heappush(pq, (next_time, next_node))

        res = [i for i in range(n + 1) if ans[i] < float('inf')]
        return res

# Example usage:
solution = Solution()
print(solution.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))  # Output: [0, 1, 2, 3, 5]
print(solution.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))  # Output: [0, 1, 3]
print(solution.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))  # Output: [0, 1, 2, 3, 4]