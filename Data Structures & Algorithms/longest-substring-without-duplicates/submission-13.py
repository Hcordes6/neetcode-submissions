class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substring = set()
        longest = 0
        
        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                longest = max(longest, r + 1 - l)
                r += 1
            else: 
                substring.remove(s[l])
                l += 1
        return longest

            