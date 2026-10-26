class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)): 
            hashmap[nums[i]] = i
        
        for j in range(len(nums)):
            rest = target-nums[j]
            ret = []
            if rest in hashmap:
                if hashmap[rest] < j:
                    ret.append(hashmap[rest])
                    ret.append(j)
                    return ret
                elif j < hashmap[rest]:
                    ret.append(j)
                    ret.append(hashmap[rest])
                    return ret
                else:
                    continue
                
                
        