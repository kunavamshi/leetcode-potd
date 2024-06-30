class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_dsu = DSU(n + 1)
        bob_dsu = DSU(n + 1)
        common_dsu = DSU(n + 1)
        
        total_edges_used = 0
        
        # Step 1: Add all type 3 edges first
        for edge in edges:
            if edge[0] == 3:
                if common_dsu.union(edge[1], edge[2]):
                    alice_dsu.union(edge[1], edge[2])
                    bob_dsu.union(edge[1], edge[2])
                    total_edges_used += 1

        # Step 2: Add type 1 and type 2 edges separately
        for edge in edges:
            if edge[0] == 1:
                if alice_dsu.union(edge[1], edge[2]):
                    total_edges_used += 1
            elif edge[0] == 2:
                if bob_dsu.union(edge[1], edge[2]):
                    total_edges_used += 1

        # Step 3: Check if both Alice's and Bob's graphs are fully traversable
        def is_fully_traversable(dsu, size):
            root = dsu.find(1)
            for i in range(2, size):
                if dsu.find(i) != root:
                    return False
            return True

        if not is_fully_traversable(alice_dsu, n + 1) or not is_fully_traversable(bob_dsu, n + 1):
            return -1
        
        # The number of removable edges is the total edges minus the edges used
        return len(edges) - total_edges_used