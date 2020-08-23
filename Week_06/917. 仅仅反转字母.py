class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s_string=[]
        for i in S:
            s_string.append(i)
        i,j=0,len(s_string)-1
        while i<j:
            while i<j and not s_string[i].isalpha():
                i+=1
            while i<j and not s_string[j].isalpha():
                j-=1
            s_string[i],s_string[j]=s_string[j],s_string[i]
            i+=1
            j-=1
        return ''.join(s_string)