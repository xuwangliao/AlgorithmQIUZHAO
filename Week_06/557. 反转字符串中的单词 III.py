class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        ans=[]
        for word in temp:
            new_word=""
            for i in range(len(word)-1,-1,-1):
                new_word+=word[i]
            ans.append(new_word)
        return ' '.join(ans)
