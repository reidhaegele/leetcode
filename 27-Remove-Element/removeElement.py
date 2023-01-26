from typing import List


class Solution:
    def removeAtEnd(self, nums: List[int], val: int):
        while (nums[-1] == val):
            nums.pop()
            if(len(nums)==0): return True
        return False

    def removeElement(self, nums: List[int], val: int) -> int:
        if(len(nums)==0): return
        if(self.removeAtEnd(nums, val)): return
        index = len(nums)-2
        while (index >= 0):
            if (nums[index] == val):
                nums[index]=nums.pop()
            index-=1

        # index = 0
        # while (index < len(nums)):
        #     if nums[index] == val:
        #         while (nums[len(nums)-1] == val):
        #             nums.pop()
        #             if (len(nums) == 0):
        #                 return

        #         if (nums[len(nums)-1] != val):
        #             nums[index] = nums[len(nums)-1]
        #             nums.pop()

        #     index += 1


if __name__ == "__main__":
    s = Solution()
    b = [3, 2, 2, 3]
    print(b)
    print("REMOVE 3")
    s.removeElement(b, 3)
    print(b)

    c = [0, 1, 2, 2, 3, 0, 4, 2]
    print(c)
    print("REMOVE 2")
    s.removeElement(c, 2)
    print(c)

    d = [1]
    print(d)
    print("REMOVE 1")
    s.removeElement(d, 1)
    print(d)

    e = []
    print(e)
    print("REMOVE 10")
    s.removeElement(e, 10)
    print(e)

    f = []
    for x in range(100):
        if(x%2==0): f.append(2)
        else: f.append(3)
    print(f)
    print("remove 3")
    s.removeElement(f, 3)
    print(f)
