class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)   # step 1: put numbers in a set
        longest = 0

        for num in nums_set:
            # start only if it's the first number of a sequence
            if num - 1 not in nums_set:
                current = num
                count = 1

                # count next numbers
                while current + 1 in nums_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest
