from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return


        # for k in range(len(nums)):
        #         for l in range(k+1,len(nums)):
        #                 if(nums[k]+nums[l]==target):
        #                         return [k,l]
        # return []
if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([2, 2], 4))
