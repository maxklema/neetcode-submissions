class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (nums[0] < nums[-1]):
            return nums[0]

        left, right = 0, len(nums) - 1
        while (left < right):
            print(left, right)
            mid = (left + right) // 2
            ro = [left, mid]
            rt = [mid + 1, right]
            if (nums[ro[0]] == nums[ro[1]] or nums[rt[0]] == nums[rt[1]]):
                return min(nums[ro[0]], nums[ro[1]], nums[rt[0]], nums[rt[1]])
            elif (nums[ro[0]] > nums[ro[1]]):
                right = mid
            else:
                left = mid + 1

        return nums[left]
