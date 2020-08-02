class Solution:
    def myPow(self, x: float, n: int) -> float:

        def myPow_helper(x, n):
            if n == 0:
                return 1.0

            y = myPow_helper(x, n // 2)
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x

        return myPow_helper(x, n) if n >= 0 else 1 / myPow_helper(x, -n)