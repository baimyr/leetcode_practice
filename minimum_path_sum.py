class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        paths = [[0 for j in range(n)] for i in range(m)]
        p = 0
        for i in range(m):
            for j in range(n):
                d1 = paths[i - 1][j] if i > 0 else None
                d2 = paths[i][j - 1] if j > 0 else None
                v = grid[i][j]
                cd = v
                if d1 is None and d2 is not None:
                    cd += d2
                if d1 is not None and d2 is None:
                    cd += d1
                if d1 is not None and d2 is not None:
                    cd += min(d1, d2)
                paths[i][j] = cd
        return paths[m - 1][n - 1]