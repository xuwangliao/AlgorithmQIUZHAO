class Solution:
    def climbStairs(self, n: int) -> int:
        #recursion + 缓存
        use = {1:1,2:2}
        def fb(n):
            if n in use:
                return use[n]
            else:
                rst = fb(n-1)+fb(n-2)
                use[n] = rst
                return use[n]
        return fb(n)