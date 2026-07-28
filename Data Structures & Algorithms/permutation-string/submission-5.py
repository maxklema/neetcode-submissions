class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        mo = {}
        for c in s1:
            if c in mo:
                mo[c] += 1
            else:
                mo[c] = 1
        
        cb = s2[0]
        ma = {}

        for idx in range(len(s1)):
            if s2[idx] in ma:
                ma[s2[idx]] += 1
            else:
                ma[s2[idx]] = 1
        
        idx=len(s1)-1
        while idx <= len(s2):
            # print(ma,mo)
            if (ma == mo):
                return True
            else:
                ma[cb] -= 1
                if ma[cb] == 0:
                    del[ma[cb]]

            if idx == len(s2)-1:
                break

            idx += 1
            if s2[idx] in ma:
                ma[s2[idx]] += 1
            else:
                ma[s2[idx]] = 1

            cb = s2[idx-len(s1)+1]
            
        return False
    
        