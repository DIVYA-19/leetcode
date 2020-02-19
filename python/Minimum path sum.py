class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)

        for i in range(1,n):
            grid[0][i] = grid[0][i] + grid[0][i-1]

        for i in range(1,m):
            for j in range(0,n):
                if j>0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                else:
                    grid[i][j] += grid[i-1][j]
        return(grid[m-1][n-1])
