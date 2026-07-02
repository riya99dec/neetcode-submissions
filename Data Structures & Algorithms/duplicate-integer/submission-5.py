class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_map={}
        for n in nums:
            prev_map[n]=1 +prev_map.get(n,0)

        for c in prev_map.values():
            if c >1:
                return True
        return False