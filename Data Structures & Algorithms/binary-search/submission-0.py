class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2

            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else: 
                return mid

        return -1



        # hi, lo, mid = len(nums) - 1, 0, math.floor((len(nums) - 1)/2)
        # print(hi, mid, lo)
        # if target == nums[mid]:
        #     return mid
        # elif lo == mid:
        #     if nums[hi] == target:
        #         return hi
        #     else:
        #         return -1
        # else:
        #     if target > mid:
        #         return self.search(nums[mid:hi+1], target)
        #     else:
        #         return self.search(nums[lo:mid], target)
