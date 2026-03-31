class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l):
            if nums.count(nums[i])<3:return nums[i]
        
