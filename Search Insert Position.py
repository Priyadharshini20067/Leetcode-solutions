class Solution(object):
    def searchInsert(self, nums, target):
        l=len(nums)
        for i in range(l):
            if nums[i]==target: return i
            elif nums[i]>target: return i
            elif i==l-1 and nums[i]<target: return i+1

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
