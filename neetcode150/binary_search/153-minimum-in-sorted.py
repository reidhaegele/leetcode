from typing import List

def findMin(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    
    if nums[l] < nums[r] or r == l:
        return nums[0]
    if r == 1:
        return nums[0] if nums[0] < nums[1] else nums[1]
    
    while l<=r:
        m = (l+r) // 2
        if nums[m-1] > nums[m]:
            return nums[m]
        else:
            if r - l == 1:
                return nums[r] 
            if nums[m] < nums[l]:
                r = m
            if nums[m] > nums[r]:
                l = m
    return nums[0]

if __name__ == '__main__':
    nums = [2, 3, 1]
    print(findMin(nums))
    nums = [4,5,6,7,0,1,2]
    print(findMin(nums))
    nums = [3,4,5,1,2]
    print(findMin(nums))
    nums = [11,13,15,17]
    print(findMin(nums))