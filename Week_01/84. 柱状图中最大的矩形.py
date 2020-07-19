class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [-1]
        n = len(heights)
        i = 0
        max_ = 0
        while i < n:
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                cur_high = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_ = max(max_, cur_high * width)
            stack.append(i)
            i += 1

        # 最后的特殊处理：
        # 如果栈非空 那么我们有单调递增栈 需要pop掉

        while len(stack) != 1:
            i = stack.pop()
            width = n - stack[-1] - 1
            max_ = max(max_, width * heights[i])
        return max_