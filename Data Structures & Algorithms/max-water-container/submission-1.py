class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front, end = 0, len(heights) - 1
        res = 0

        while (front < end):
            front_height = heights[front]
            end_height = heights[end]
            area = min(front_height, end_height) * (end - front)
            res = max(area, res)

            if (front_height < end_height):
                front += 1
            else:
                end -= 1

        return res        