class Solution(object):
    def romanToInt(self, s):
        s=s+'p'
        l=len(s)
        n,i=0,0
        while(i<l-1):
            if s[i]=='I':
                if s[i+1]=='V':
                    n=n+4
                    i=i+2
                elif s[i+1]=='X':
                    n=n+9
                    i=i+2
                else:
                    n=n+1
                    i=i+1
                    print(n)
            elif s[i]=='X':
                if s[i+1]=='L':
                    n=n+40
                    i=i+2
                elif s[i+1]=='C':
                    n=n+90
                    i=i+2
                else:
                    n=n+10
                    i=i+1
            elif s[i]=='C':
                if s[i+1]=='D':
                    n=n+400
                    i=i+2
                elif s[i+1]=='M':
                    n=n+900
                    i=i+2
                else:
                    n=n+100
                    i=i+1
            elif s[i]=='M':
                n=n+1000
                i=i+1
            elif s[i]=='V':
                n=n+5
                i=i+1
            elif s[i]=='L':
                n=n+50
                i=i+1
            else: 
                n=n+500
                i=i+1
        return n
        """
        :type s: str
        :rtype: int
        """
        
