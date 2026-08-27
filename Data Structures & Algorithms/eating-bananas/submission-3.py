import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        num_piles = len(piles)
        maximum = 0 # maximum pile size
        for pile in piles:
            maximum = max(maximum, pile)
        
        # binary search
        start = 1
        end = maximum
    
        while (start <= end):
            mid = (start + end) // 2
            total_hours = 0
            for i in range(len(piles)):
                total_hours += math.ceil(piles[i] / mid) 
            if (total_hours <= h):
                end = mid - 1
            else:
                start = mid + 1

        print(f"{start} {end}")
        return start
        