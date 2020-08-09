class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1,0]

        dp[0] = 1
        dp[1] = 1 if s[0]!="0" else 0
        for i in range(1,n):
            dp.append(0)
            if 10 < int(s[i-1]+s[i]) <= 26 and int(s[i]) != 0:
                dp[-1] = dp[-2]+dp[-3]
            elif 10 <= int(s[i-1]+s[i]) <= 26:
                dp[-1] = dp[-3]
            elif int(s[i]) != 0:
                dp[-1] = dp[-2]
        return dp[-1]