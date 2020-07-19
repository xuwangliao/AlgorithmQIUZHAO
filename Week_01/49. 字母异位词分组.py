class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            sort = sorted(list(string))
            hashmap[tuple(sort)] = hashmap.get(tuple(sort), []) + [string]

        return list(hashmap.values())