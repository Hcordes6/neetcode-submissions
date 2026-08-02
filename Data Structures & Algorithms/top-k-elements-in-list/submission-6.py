class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ret = []
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in range(k):
            currentMax = None
            for index, j in enumerate(hashmap):
                if index == 0:
                    currentMax = j
                    print(currentMax)
                if hashmap[j] > hashmap[currentMax]:
                    currentMax = j
                print(f"Value of j at {index} is {hashmap[j]}")
                print(f"Max after index: {index} is {currentMax}")
            ret.append(currentMax)
            print(f"{currentMax} {i}")
            hashmap.pop(currentMax)
        return ret
            
