class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(z):
            a=[]
            for i in z:
                if(i != '#'):
                    a.append(i)

                else:
                    if len(a)!=0:
                        a.pop()
            return a

        return check(s)==check(t)