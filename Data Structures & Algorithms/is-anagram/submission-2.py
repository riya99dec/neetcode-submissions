class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {},{}
        if len(s)!=len(t):
            return False
        else:
            for i, n in enumerate(s):
                countS[n]=1 + countS.get(n,0)
            for i,n in enumerate(t):
                countT[n]=1 + countT.get(n,0)
            for i,n in enumerate(countS):
                if countS[n]!=countT.get(n,0):
                    return False
            return True