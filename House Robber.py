class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        b=[]
        for i in range(l):
            if i==0:b.append(nums[i])
            elif i==1:b.append(max(nums[0],nums[i]))
            else:b.append(max(nums[i]+b[i-2],b[i-1]))
        return max(b)
