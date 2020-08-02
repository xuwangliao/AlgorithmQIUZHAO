class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(x, y):
            if grid[x][y] == "1":
                grid[x][y] = "0"
                for neighbor in neighbors:
                    nex_x, nex_y = x + neighbor[0], y + neighbor[1]
                    if 0 <= nex_x < len(grid) and 0 <= nex_y < len(grid[0]):
                        dfs(nex_x, nex_y)
            else:
                return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count