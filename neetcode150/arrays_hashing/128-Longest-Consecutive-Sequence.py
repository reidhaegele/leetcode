class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        m = 0
        for x in nums:
            if x-1 not in numSet:
                length = 1
                while(x + length in numSet):
                    length+=1
                if m < length:
                    m = length
        
        return m