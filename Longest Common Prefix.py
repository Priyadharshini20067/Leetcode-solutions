class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        b=len(strs)
        l=len(strs[0])
        n,c=0,0
        j=""
        b=len(strs)
        l=len(strs[0])
        n,c=0,0
        j=""
        while n<l:
            j=j+strs[0][n]
            for i in strs:
                if i.startswith(j):
                    c=c+1
                if c==b:
                    a=j
            c=0
            n=n+1      
        return a
              
