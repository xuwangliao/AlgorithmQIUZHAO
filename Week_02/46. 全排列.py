class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        def helper(nums,path):
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(len(nums)):
                path.append(nums[i])
                helper(nums[:i]+nums[i+1:],path)
                path.pop()
        helper(nums,[])
        return res