class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(nums, path):
            self.res.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[i + 1:], path)
                path.pop()

        dfs(nums, [])
        return self.res

        # res = [[]]

        # for num in nums:
        #    res = res + [ele + [num] for ele in res]
        # return res