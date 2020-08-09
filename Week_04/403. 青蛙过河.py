class Solution:
    def canCross(self, stones: List[int]) -> bool:
        hashmap = {}
        for i in range(len(stones)):
            hashmap[stones[i]] = set()
        stones_set = set(stones)
        hashmap[0].add(0)
        moves = [-1, 0, 1]
        for i in range(len(stones) - 1):
            for k in hashmap[stones[i]]:
                for move in moves:
                    next_pos = stones[i] + k + move
                    if next_pos > stones[i] and next_pos in stones_set:
                        hashmap[next_pos].add(k + move)

        return True if hashmap[stones[-1]] else False