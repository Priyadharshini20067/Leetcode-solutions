class Solution(object):
    def isValid(self, s):
        l=len(s)
        s1=list(s)
        b=[]
        for i in range(l):
            a=s[i]
            if a=='(' or a=='[' or a=='{':
                b.append(a)
            else:
                if not b:return False
                else:s2=b[-1]
                if (a==')' and s2=='(')  or (a==']' and s2=='[') or (a=='}' and s2=='{'):
                    b.pop()
                else:return False
        if not b:return True
        else:return False
        
