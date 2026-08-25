import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq.setdefault(nums[i], [0, nums[i]])
            freq[nums[i]][0] -= 1

        vals_heap = list(freq.values())
        heapq.heapify(vals_heap,)
        
        return [heapq.heappop(vals_heap)[1] for x in range(0,k)]