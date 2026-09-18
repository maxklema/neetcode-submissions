class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        most_freq = s[0]
        most_freq_count = 1
        freq = {s[0]: 1}
        left, right = 0, 1

        while (right != len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1   
            if (freq[s[right]] > most_freq_count):
                most_freq = s[right]
                most_freq_count = freq[s[right]]
            
            # make sure still under k

            def custom_sort(n):
                return n[1]

            vals = sorted(freq.items(), key=custom_sort, reverse=True)
            count = 0
            for i in range(1,len(freq)):
                count += vals[i][1]

            while (k < count):
                freq[s[left]] = max(0, freq[s[left]] - 1)
                if (s[left] == 0):
                    freq.pop(s[left])
            
                vals = sorted(freq.items(), key=custom_sort, reverse=True)
                count = 0
                for i in range(1,len(freq)):
                    count += vals[i][1]

                left += 1
          
            res = max(res, ((right - left) + 1))
            right += 1

        return res