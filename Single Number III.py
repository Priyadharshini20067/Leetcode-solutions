class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=len(nums)
        a=[]
        for i in range(l):
            if nums.count(nums[i])<2:a.append(nums[i])
        return a
        
