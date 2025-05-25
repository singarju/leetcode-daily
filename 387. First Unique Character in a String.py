class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        a={chr(i): -1 for i in range (ord('a'), ord('z')+1)}
        m=len(a)
        for j in range (0,n):
            a[s[j]]=a[s[j]]+1
        for k in range(0,n):
            if a[s[k]]==0:
                return k
        return -1