import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            from_city, to_city, price = flight
            if from_city not in graph:
                graph[from_city] = []
            graph[from_city].append((to_city, price))
        
        memo = {}  # Memoization dictionary to store computed prices
        
        def dfs(city, stops):
            if city == dst:
                return 0
            if stops > k:
                return float('inf')
            if (city, stops) in memo:
                return memo[(city, stops)]
            
            min_price = float('inf')
            if city in graph:
                for neighbor, price in graph[city]:
                    min_price = min(min_price, price + dfs(neighbor, stops + 1))
            
            memo[(city, stops)] = min_price
            return min_price
        
        result = dfs(src, 0)
        return result if result != float('inf') else -1