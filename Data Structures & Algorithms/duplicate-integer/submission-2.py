class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countT={}
        for n in nums:
            countT[n]= 1+ countT.get(n,0)
        
        for n in countT.values():
            if n>1:
                print(n)
                return True
        else:
            return False
        
        