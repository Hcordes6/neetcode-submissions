class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        #print(nums)
        currentHighest = 1
        tempHighest = 1
        for i in range(1, len(nums)):
            #print(f"iteration:{i} is nums value {nums[i]} with current highest {currentHighest} and temp {tempHighest}")
            if nums[i] == (nums[i-1] + 1):
                tempHighest += 1
            elif nums[i] == nums[i-1]:
                continue
            elif tempHighest > currentHighest:
                currentHighest = tempHighest
                tempHighest = 1
            else:
                tempHighest = 1
        if tempHighest > currentHighest:
            currentHighest = tempHighest
        return currentHighest
