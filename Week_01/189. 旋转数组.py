class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        nums[:] = nums[::-1]
        return nums
