class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while (top <= bottom):
            middle = (top + bottom) // 2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break

        row = (top + bottom) // 2
            
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
