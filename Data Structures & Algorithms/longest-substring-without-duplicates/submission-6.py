class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        res_set = set([])
        left, right = 0, 0

        while right < len(s):
            valueIncluded = s[right] in res_set
            if not valueIncluded:
                res_set.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                if (right == len(s) - 1):
                    break
                res_set.remove(s[left])
                left += 1

        return res
