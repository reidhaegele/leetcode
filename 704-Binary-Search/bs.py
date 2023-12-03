def search(nums, target) -> int:
    index = len(nums) // 2
    while nums[index] != target:
        if (target > nums[index]):
            if (index+1 >= len(nums)):
                return -1
            if (target < nums[index+1]):
                return -1
            index += index // 2
        else:
            if (index-1 <= -1):
                return -1
            if (target > nums[index-1]):
                return -1
            index -= index // 2
    return index
    

if __name__ == '__main__':
    nums = [2, 5]
    print(search(nums, 2))