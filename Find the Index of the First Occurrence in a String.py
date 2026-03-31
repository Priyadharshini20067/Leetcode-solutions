class Solution(object):
    def strStr(self, haystack, needle):
        l=len(needle)
        l1=len(haystack)
        i=0
        if needle in haystack:
            while(i<=l1):
                if haystack[i]==needle[0]:
                    if haystack[i:i+l]==needle:return i
                i=i+1
        else:
            return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
