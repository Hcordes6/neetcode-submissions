class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in s:
            if i not in dict_s:
                dict_s.update({i : 0})
            else:
                dict_s.update({i : dict_s[i] + 1})
        for i in t:
            if i not in dict_t:
                dict_t.update({i : 0})
            else:
                dict_t.update({i : dict_t[i] + 1})
        return dict_s == dict_t
