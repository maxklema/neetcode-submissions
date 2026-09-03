class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        res_set = set([])
        left, right = 0, 0
        n = len(s)

        while right < n:
            if s[right] not in res_set:
                res_set.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                res_set.remove(s[left])
                left += 1

        return res
