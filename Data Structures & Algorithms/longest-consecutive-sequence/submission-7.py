class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        hm = {}
        for num in nums:
            start = hm.get(num - 1, [num, num])[0]
            end = hm.get(num + 1, [num, num])[1]
            hm[start] = [start, end]
            hm[end] = [start, end]
            res = max(end - start + 1, res)
        return res
