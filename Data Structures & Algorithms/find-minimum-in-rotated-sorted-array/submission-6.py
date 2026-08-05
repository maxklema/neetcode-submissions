class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if nums[0] < nums[size - 1]:
            return nums[0]

        left = 0
        right = size - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        return nums[right]
