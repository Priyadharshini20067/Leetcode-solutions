class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        a=[]
        for i in range(n):
            a.append(l1[i])
            a.append(l2[i])
        return a

        
