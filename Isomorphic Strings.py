class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        l1=len(s)
        l2=len(t)
        for i in range(l1):
            if s[i] not in d1:
                d1[s[i]]=t[i]
            else:
                if d1[s[i]]!=t[i]:return False
        for i in range(l2):
            if t[i] not in d2:
                d2[t[i]]=s[i]
            else:
                if d2[t[i]]!=s[i]:return False
        return True
