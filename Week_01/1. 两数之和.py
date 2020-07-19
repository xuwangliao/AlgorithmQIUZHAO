class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i,num in enumerate(nums):
            if target - num not in dic:
                dic[num] = i
            else:
                return [dic[target - num],i]