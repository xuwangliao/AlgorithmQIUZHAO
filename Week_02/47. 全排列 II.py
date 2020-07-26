class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        def helper(nums,path):
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i>0 and nums[i]== nums[i-1]:
                    continue
                path.append(nums[i])
                helper(nums[:i]+nums[i+1:],path)
                path.pop()

        helper(nums,[])
        return res