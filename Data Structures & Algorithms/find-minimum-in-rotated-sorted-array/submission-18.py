class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (nums[0] < nums[-1]):
            return nums[0]

        left, right = 0, len(nums) - 1
        while (left < right - 1):
            print(left, right)
            mid = (left + right) // 2
            if (nums[left] <= nums[right]):
                return nums[left]
            elif (nums[mid] >= nums[left]):
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])