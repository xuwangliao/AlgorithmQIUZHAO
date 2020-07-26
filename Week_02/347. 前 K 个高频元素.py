class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        return heapq.nlargest(k, count.keys(), key=lambda x: count[x])