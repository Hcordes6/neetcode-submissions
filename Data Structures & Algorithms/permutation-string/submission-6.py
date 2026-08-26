class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a hashmap of each char and its counts
        # Then use sliding window to check each window of length s1 until we find a match if any

        l = 0
        counts1 = {}
        counts2 = {}
        countsChanged = False

        #init counts
        for i in s1:
            counts1[i] = counts1.get(i, 0) + 1

        for r in range(len(s2)):
            counts2[s2[r]] = counts2.get(s2[r], 0) + 1

            if (r - l + 1) == len(s1):
                if counts1 == counts2:
                    return True
                else:
                    counts2[s2[l]] -= 1
                    if counts2[s2[l]] == 0:
                        del counts2[s2[l]]
                    l += 1
        return False

            

        
                
            

#  for r in range(len(s2)):
#             if counts.get(s2[r]) and counts[s2[r]] > 0:
#                 counts[s2[r]] -= 1
#                 countsChanged = True
#             elif counts.get(s2[r]) and counts[s2[r]] == 0:
#                 while counts[s2[r]] == 0:
#                     counts[s2[l]] = counts.get(s2[l], 0) + 1
#                     l += 1
#             elif max(counts.values()) == 0:
#                 #if the hashmap is empty then true
#                 return True
#             elif countsChanged:
#                 #if its not empty then we need to reset it according to the chars within the window. Then we can set l = r.
#                 while l < r:
#                     counts[s2[l]] = counts.get(s2[l], 0) + 1
#                     l += 1
#                 countsChanged = False
#             else: 
#                 l = r + 1
#         return False