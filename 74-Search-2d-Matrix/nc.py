from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
                        
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right = mid - 1
            if matrix[row][col] < target:
                left = mid + 1

        return False