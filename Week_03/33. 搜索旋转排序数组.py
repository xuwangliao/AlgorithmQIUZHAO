class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            nums_mid = nums[mid]
            if nums_mid == target:
                return mid
            if nums_mid >= nums[0]:
                if nums[0] <= target < nums_mid:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums_mid < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
