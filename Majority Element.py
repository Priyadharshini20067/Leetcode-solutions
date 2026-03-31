class Solution(object):
    def majorityElement(self, nums):
        a=list(set(nums))
        m=0
        for i in a:
            a=nums.count(i)
            if(a>m):
                m=a
                maj=i
        return maj
        
