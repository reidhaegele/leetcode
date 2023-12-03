class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if not nums:
            return -1
        
        left = 0
        right = length - 1

        if length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while(left <= right):
            temp = (left + right) // 2
            if nums[temp] == target:
                return temp
            elif nums[temp] > target:
                right = temp - 1
            elif nums[temp] < target:
                left = temp + 1
        return -1