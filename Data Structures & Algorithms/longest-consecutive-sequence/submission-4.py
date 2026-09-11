class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hm = {}
        for num in nums:
            if num not in hm:
                start = hm.get(num-1,[num,num])[0]
                end = hm.get(num+1,[num,num])[1]
                hm[num] = [start,end]
                hm[start][1] = end
                hm[end][0] = start
                res = max(end - start + 1, res)
        return res 