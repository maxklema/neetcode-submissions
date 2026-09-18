class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        freq = {s[0]: 1}
        left, right = 0, 1

        while (right != len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1   
            
            # make sure still under k

            def custom_sort(n):
                return n[1]

            vals = sorted(freq.items(), key=custom_sort, reverse=True)
            count = ((right - left) + 1) - vals[0][1]
            # print(f"count: {count}, {right - left + 1}, {vals[0][1]}")

            while (k < count):
                freq[s[left]] = max(0, freq[s[left]] - 1)
                if (s[left] == 0):
                    freq.pop(s[left])
                
                # if (s[left] == most_freq):
                vals = sorted(freq.items(), key=custom_sort, reverse=True)
                # print(vals)
                left += 1
                count = max(0, ((right - left) + 1) - vals[0][1])
                # print(count)
          
            res = max(res, ((right - left) + 1))
            right += 1

        return res