class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        # Ex for reference [3, 4, 5, 1, 2]
        # Ex for reference [3, 4, 5, 6, 7, 8, 1, 2]
        # Ex for reference [6, 7, 1, 2, 3, 4, 5]
        while lo <= hi:
            mid = (hi + lo) // 2

            if target == nums[mid]:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[mid] > target and target >= nums[lo]:
                    hi = mid - 1
                else: 
                    lo = mid + 1
            else:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


