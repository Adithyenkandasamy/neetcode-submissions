class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        m = c.most_common(k)
        ans = []
        for i in m:
            ans.append(i[0])
        return ans        