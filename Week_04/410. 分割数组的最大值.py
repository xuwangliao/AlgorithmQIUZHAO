class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        l, r = max(nums), sum(nums)

        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            temp = 0
            for i in range(len(nums)):
                if temp + nums[i] > mid:
                    temp = nums[i]
                    cnt += 1
                else:
                    temp += nums[i]
            if cnt >= m:
                l = mid + 1
            else:
                r = mid - 1
        return l