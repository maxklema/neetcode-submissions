class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        nums = sorted(nums)
        res = 0
        current = 1
        for i in range(1, len(nums)):
            res = max(res, current)
            if nums[i - 1] + 1 == nums[i]:
                current += 1
                continue
            elif nums[i - 1] == nums[i]:
                continue
            else:
                current = 1

        return max(res, current)
