class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]]=1
            else:
                count[s[i]]+=1
        for j in range(len(s)):
            if count[s[j]]==1:
                return j
        return -1