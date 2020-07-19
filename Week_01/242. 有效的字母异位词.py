class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}

        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        for c in t:
            if c not in dic:
                return False
            else:
                if dic[c] == 0:
                    return False
                else:
                    dic[c] -= 1
        return True