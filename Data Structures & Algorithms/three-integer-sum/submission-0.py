class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # O(nlogn)

        res = set()
        pin = 0

        for pin_num in range(len(nums) - 2): #O(n)
            start = pin_num + 1
            end = len(nums) - 1
            target = 0 - nums[pin_num]
            while (start < end): # O(n)
                current = nums[end] + nums[start]
                if (current == target):
                    res.add(tuple([nums[pin_num], nums[start], nums[end]]))
                    start += 1
                    end -= 1
                elif (current < target):
                    start += 1
                else:
                    end -= 1
        
        return list(list(_) for _ in res)
