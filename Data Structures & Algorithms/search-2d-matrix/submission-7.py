class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = None
        if (right == 0):
            row = 0
        else:
            while (True):
                mid = (left + right) // 2
                mid_val = matrix[mid][0] 
                if right - left == 1 or right == left:
                    break
                elif mid_val > target:
                    right = mid
                else:
                    left = mid
        if (matrix[left][0] <= target and matrix[right][0] > target):
            row = left
        else:
            row = right
            
        left, right = 0, len(matrix[row]) - 1
        while (left <= right):
            mid = (left + right) // 2
            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] > target):
                right = mid - 1
            else:
                left = mid + 1

        return False
