class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        c=0
        s=""
        while i>=0 or j>=0 or c:
            if i>=0:
                c=c+int(a[i])
                i=i-1
            if j>=0:
                c=c+int(b[j])
                j=j-1
            s=s+str(c%2)
            c=c//2
        return s[::-1]

       
        
