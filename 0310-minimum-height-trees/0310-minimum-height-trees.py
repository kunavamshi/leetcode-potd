from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, so it's already an MHT
        
        # Construct the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize leaves list with nodes having only one neighbor
        leaves = deque([node for node in range(n) if len(graph[node]) == 1])
        
        # Continue removing leaves until only the MHT roots remain
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                neighbor = graph[leaf].pop()  # Remove the leaf from its neighbor's list
                graph[neighbor].remove(leaf)  # Remove the neighbor from the leaf's list
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return list(leaves)