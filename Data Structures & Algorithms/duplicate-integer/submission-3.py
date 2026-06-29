class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countT={}
        for i,n in enumerate(nums):
            if n in countT:
                return True
            countT[n]=i
        return False

        
        