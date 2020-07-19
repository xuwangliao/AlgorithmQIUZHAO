class Solution:
    def trap(self, height: List[int]) -> int:

        # 单调递减栈
        stack = [-1]

        i = 0
        n = len(height)
        ans = 0
        while i < n:
            while len(stack) > 1 and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if stack[-1] != -1:
                    h = min (height[stack[-1]],height[i]) - height[cur]
                    ans += h * (i-stack[-1]-1)
            stack.append(i)
            i+= 1
        return ans