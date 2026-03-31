class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        c=1
        j=0
        nums[j]=nums[0]
        for i in range(l-1):
            if(nums[i]<nums[i+1]):
                c=c+1
                j=j+1
                nums[j]=nums[i+1]    
        return c
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
