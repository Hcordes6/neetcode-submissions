class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        charSet = set()
        longest = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1

        return longest
