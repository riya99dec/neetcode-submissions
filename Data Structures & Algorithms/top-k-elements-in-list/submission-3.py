class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for n in nums:
            count[n]=1+count.get(n,0)
        count_dict = dict(sorted(count.items(), key = lambda x:x[1], reverse = True))
        countList = list(count_dict.keys())
        return countList[:k]