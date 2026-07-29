class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}
        for i in s:
            if i in hashmapS:
                hashmapS.update({i : hashmapS[i] + 1})
            else:
                hashmapS.update({i:1})
        for j in t:
            if j in hashmapT:
                hashmapT.update({j:hashmapT[j] + 1})
            else:
                hashmapT.update({j:1})
        for k in hashmapS:
            if k not in hashmapT and hashmapS[k] != 0:
                return False
            if hashmapS[k] != hashmapT[k]:
                return False
        for l in hashmapT:
            if l not in hashmapS and hashmapT[l] != 0:
                return False
            if hashmapT[l] != hashmapS[l]:
                return False
        return True
