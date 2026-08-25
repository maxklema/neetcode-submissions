import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = [freq.get(nums[i], [0, nums[i]])[0] - 1, nums[i]]

        vals_heap = list(freq.values())
        heapq.heapify(vals_heap,)
        
        return [heapq.heappop(vals_heap)[1] for x in range(0,k)]