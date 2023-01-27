from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        while (digits[index]+1 == 10):
            digits[index] = 0
            index -= 1
            if (index < 0):
                digits.insert(0, 1)
                return digits
        digits[index] = digits[index]+1
        return digits


if __name__ == "__main__":
    s = Solution()

    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([1, 2, 9]))
    print(s.plusOne([1, 9]))
    print(s.plusOne([9, 9, 9]))
    print(s.plusOne([9]))
    print(s.plusOne([9, 9, 1, 1, 9, 9, 9, 9, 2, 9, 3, 9, 4, 9]))
