class Solution:
    def reverseWords(self, s: str) -> str:
        tmp=s.split()
        return ' '.join(tmp[::-1])
