class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g_len = len(g)
        s_len = len(s)
        i = j = 0
        g.sort()
        s.sort()
        while i<g_len and j < s_len:
            if s[j]>=g[i]:
                i += 1
            j+=1
        return i