class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_ = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] > max_:
                max_ = dp[i][0]
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] > max_:
                max_ = dp[0][j]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                if dp[i][j]>max_:
                    max_ = dp[i][j]
        return max_**2