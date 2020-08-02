class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #思路 双指针 遍历t跟s，当s跑完，t没跑完就成功，否则失败
        len_s = len(s)
        len_t = len(t)
        #i point to s
        i = 0
        #j point to t
        j = 0
        while  i < len_s and j <len_t:
            if s[i] == t[j]:
                i+=1
            j+=1
        return i>=len_s