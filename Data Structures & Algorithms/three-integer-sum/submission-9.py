class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        # for loop
            # i stays at index 
                #now we essentially run two sum II on this set
                # two pointers, one at beginning one at end
                # target value is -i
                # if their sum is larger than target value, decrement end pointer
                # if smaller increment begin pointer
                # repeat on each index
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            print(f"round: {nums[i]}")
            j, k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                if j == i:
                    j += 1
                elif k == i:
                    k -= 1
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    ret.append(triplet)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return ret