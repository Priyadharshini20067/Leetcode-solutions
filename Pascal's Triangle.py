class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows-1
        b=[]
        a=[[1]]
        if numRows==0:return a
        for i in range(1,numRows):
            for j in range(numRows):
                if i>=j:
                    if j==0:
                        b.append(1)
                    elif j==i:
                        b.append(1)
                    else:
                        b.append(a[i-1][j-1]+a[i-1][j])
            a.append(b)
            b=[]
        return a
                     
                    
            
