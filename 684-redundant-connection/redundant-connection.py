#sync with github
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = list(range(len(edges) + 1))  # DSU parent array
        rank = [0] * (len(edges) + 1)  # Rank array for union optimization

        def find(x):
            """Find the representative (root) of set x with path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            """Union by rank. Returns False if x and y are already connected (cycle detected)."""
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # Cycle detected
            if rank[rootX] > rank[rootY]:  # Attach smaller tree to larger tree
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]  # This is the redundant edge

# Example usage:
sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))  # Output: [2,3]
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # Output: [1,4]
