class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num] = 1+ count.get(num,0)
        countdict = dict(sorted(count.items(),key = lambda x:x[1],reverse = True))
        CountList = list(countdict.keys())
        return CountList[:k]
            