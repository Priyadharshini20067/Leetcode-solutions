class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        b=[]
        a=[[1]]
        for i in range(1,rowIndex+1):
            for j in range(rowIndex+1):
                if i>=j:
                    if j==0:
                        b.append(1)
                    elif j==i:
                        b.append(1)
                    else:
                        b.append(a[i-1][j-1]+a[i-1][j])
            a.append(b)
            b=[]
        return a[rowIndex]

        
