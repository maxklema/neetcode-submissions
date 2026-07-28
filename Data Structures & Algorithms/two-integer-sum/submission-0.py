class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if (remaining in map):
                return [map[remaining], i]
            else:
                map[nums[i]] = i