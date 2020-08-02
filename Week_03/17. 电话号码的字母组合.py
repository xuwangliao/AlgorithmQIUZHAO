class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        self.res = []

        def dfs(digits, path, index):
            if index == n:
                self.res.append(path[:])
                return

            for char in phone_map[digits[index]]:
                dfs(digits, path + char, index + 1)

        dfs(digits, "", 0)
        return self.res