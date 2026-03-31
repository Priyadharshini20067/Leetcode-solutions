class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=list(s.split(" "))
        if len(set(a))!=len(set(list(pattern))):
            return False
        if len(a)!=len(list(pattern)):return False
        c={}
        for i in range(len(pattern)):
            if pattern[i] not in c:
                c[pattern[i]]=a[i]
            else:
                if c[pattern[i]]!=a[i]:
                    return False
        return True
        
