class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,i,j = [0]*len(nums),0,0
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                product *=nums[j]
            res[i]=product
        return res