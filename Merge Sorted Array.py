class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k=0
        for i in range(m):
            nums1[k]=nums1[i]
            k=k+1
        for j in range(n):
            if(nums2[j]!=0):
                nums1[k]=nums2[j]
                k=k+1
        print(nums1.sort())
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
