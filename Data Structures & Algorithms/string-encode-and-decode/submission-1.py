class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += f"#{len(string)}#{string}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 1
        while idx < len(s):
            # get num chars
            num_chars = ""
            print(s[idx])
            while (s[idx] != "#"):
                num_chars += s[idx]
                idx += 1
            print(num_chars)
            num_chars = int(num_chars)
            word = ""
            for i in range(num_chars):
                word += s[idx + i + 1]
            res.append(word)
            idx += (2 + num_chars)
        return res
