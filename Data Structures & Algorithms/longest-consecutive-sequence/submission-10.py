class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hm = {}
        for num in nums:
           
            start = hm.get(num-1,[num,num])[0]
            end = hm.get(num+1,[num,num])[1]
            hm[num] = [start, end]
            hm[start] = [start, end]
            hm[end] = [start, end]
            # print(hm)
            res = max(end - start + 1, res)
        return res  