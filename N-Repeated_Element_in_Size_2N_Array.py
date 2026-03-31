class Solution(object):
    def repeatedNTimes(self, nums):
        a=list(set(nums))
        m=0
        for i in a:
            c=nums.count(i)
            if m<c:
                m=c
                maj=i
        return maj

        """
        :type nums: List[int]
        :rtype: int
        """
        
