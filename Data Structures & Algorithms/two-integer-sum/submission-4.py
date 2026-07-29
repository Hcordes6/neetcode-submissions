class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        ret = []
        for i in range(len(nums)):
            if nums[i] in hashmap:
                ret.append(hashmap[nums[i]])
                ret.append(i)
                return ret
            else:
                hashmap.update({nums[i] : i})
        for i in range(len(nums)):
            var = target - nums[i]
            if var in hashmap and nums[i] in hashmap:
                if hashmap[nums[i]] > hashmap[var]:
                    ret.append(hashmap[var])
                    ret.append(hashmap[nums[i]])
                    break
                elif hashmap[nums[i]] < hashmap[var]:
                    ret.append(hashmap[nums[i]])
                    ret.append(hashmap[var])
                    break
        return ret