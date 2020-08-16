class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {
            1: 1,
            2: 2
        }

        def dfs(n):
            if n in dic:
                return dic[n]
            else:
                dic[n] = dfs(n - 1) + dfs(n - 2)
                return dic[n]

        return dfs(n)