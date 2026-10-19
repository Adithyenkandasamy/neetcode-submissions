from typing import List
from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, count in counts.items():
            if count > 1:
                return num
