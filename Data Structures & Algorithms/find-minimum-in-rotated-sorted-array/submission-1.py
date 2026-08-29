class Solution:
    def findMin(self, nums: List[int]) -> int:
        # BS would still work with slight modifications. 

        lowest = nums[0]

        hi, lo = len(nums) - 1, 0
        end = False
        while lo <= hi:
            mid = (hi + lo) // 2

            lowest = min(nums[mid], lowest)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else: #because iitems are unique
                hi = mid - 1
                
        return lowest
            # if hi > lo: 
            #     if(hi != len(nums) - 1):
            #         return nums[hi + 1]
            #     else
            #         return lo
            # else:
            #     # Run BS and find highest element, it will be one after it
                

