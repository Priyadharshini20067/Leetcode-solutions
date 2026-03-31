class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=len(s)
        c=0
        for i in range(l):
            if s[i-1]==" " and s[i]!=" ":
                c=0
            if s[i]!=" ":
                c=c+1
        return c
