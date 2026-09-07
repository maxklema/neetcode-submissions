class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1
        while (bottom <= top):
            middle = (top + bottom) // 2
            if target < matrix[middle][0]:
                top = middle - 1
            elif target > matrix[middle][-1]:
                bottom = middle + 1
            else:
                break

        if (top < bottom):
            return False
        
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
