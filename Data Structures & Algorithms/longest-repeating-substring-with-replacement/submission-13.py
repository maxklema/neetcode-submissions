class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        mfq = s[0]
        mfqc = 1
        freq = {s[0]: 1}
        left, right = 0, 1

        while (right != len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1   
            if (s[right] == mfq):
                mfqc += 1
            elif (s[right] != mfq and freq[s[right]] > mfqc):
                mfq = s[right]
                mfqc = freq[s[right]] 

            count = ((right - left) + 1) - mfqc

            while (k < count):
                freq[s[left]] = max(0, freq[s[left]] - 1)
                if (s[left] == 0):
                    freq.pop(s[left])
                
                left += 1
                count = max(0, ((right - left) + 1) - mfqc)

            mfqc = freq[mfq]
            res = max(res, ((right - left) + 1))
            right += 1

        return res