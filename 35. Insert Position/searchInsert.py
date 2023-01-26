from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in nums:
                if(i < target): index+=1
                elif(i >= target): break
        return index