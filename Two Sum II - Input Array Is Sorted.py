class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        sum=0
        while(1):
            sum=numbers[l]+numbers[r]
            if sum<target:l=l+1
            elif sum>target:r=r-1
            else:break
        return [l+1,r+1]
