class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq.setdefault(nums[i], [0, nums[i]])
            freq[nums[i]][0] += 1

        vals_sorted = sorted(freq.values())
        vals_sorted = vals_sorted[::-1]

        return [vals_sorted[i][1] for i in range(0, k)]
