class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        assign={}
        used = set()
        for i in range(len(s)):
            if s[i] not in assign:
                if t[i] not in used:
                    assign[s[i]]=t[i]
                    used.add(t[i])
                else:
                    return False
            elif assign[s[i]]!=t[i]:
                    return False
        return True