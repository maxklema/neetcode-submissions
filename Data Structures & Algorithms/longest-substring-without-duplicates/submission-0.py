class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        map = {}

        left, right = 0, 0
        while right < len(s):
            value = map.get(s[right], 0)
            if value == 0:
                map[s[right]] = 1
                res = max(res, right - left + 1)
                right += 1
            else:
                map[s[left]] = map[s[left]] - 1
    
                left += 1

        return res
