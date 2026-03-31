class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=list(set(nums))
        l1=len(nums)
        l2=len(num)
        if(l1>l2):
            return True
        else:
            return False

        
