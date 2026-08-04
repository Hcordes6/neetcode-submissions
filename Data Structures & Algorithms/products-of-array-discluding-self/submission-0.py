class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        ret = []
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            prefix.append(prod)
        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            prod = prod * nums[j]
            suffix.insert(0, prod)
        print(prefix)
        print(suffix)
        for k in range(len(nums)):
            if k == 0:
                ret.append(1 * suffix[k + 1])
            elif k == len(nums) - 1:
                ret.append(prefix[k - 1] * 1)
            else:
                ret.append(prefix[k - 1] * suffix[k + 1])
        return ret