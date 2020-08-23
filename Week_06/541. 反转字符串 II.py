class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        index=0
        s_string = []
        for i in s:
            s_string.append(i)
        while index < n:
            if n//(2*k) >= 1 or n//k >= 1:
            #swap the first k element and update index
                s_string[index:index+k]=s_string[index:index+k][::-1]
            elif n//k == 0:
                s_string[index:]=s_string[index:][::-1]
            index+=2*k
        return ''.join(s_string)