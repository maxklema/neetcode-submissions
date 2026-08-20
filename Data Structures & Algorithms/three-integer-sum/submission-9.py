class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # O(nlogn)

        res = []

        for pin_num in range(len(nums) - 2): #O(n)
            if pin_num > 0 and nums[pin_num] == nums[pin_num - 1]:
                continue

            start = pin_num + 1
            end = len(nums) - 1
            target = 0 - nums[pin_num]
            while (start < end): # O(n)
                current = nums[end] + nums[start]
                if (current == target):
                    res.append([nums[pin_num], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif (current < target):
                    start += 1
                else:
                    end -= 1
        
        return res
