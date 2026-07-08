from typing import List
from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Count frequencies of each number
        counts = Counter(nums)
        
        # Find the number with a count greater than 1
        for num, count in counts.items():
            if count > 1:
                return num
