class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        for i,num in enumerate(nums):
            heappush(h,(-num,i))
            if i-k+1>=0:
                while h and h[0][1]<=i-k: heappop(h)
                res.append(-h[0][0])
        return res