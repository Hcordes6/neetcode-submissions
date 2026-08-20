import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Binary search, take half the problem set at a time. 
        # Begin by dividing target in half and search two pointer at each half? 
        
        ret = []

        for i in range(len(numbers)):
            num2 = target - numbers[i]
            # Built in binary search for python.
            # Returns index (right of duplicate)
            searchIndex = bisect.bisect(numbers, num2, i, len(numbers))
            if numbers[searchIndex - 1] == num2:
                ret.append(i + 1)
                ret.append(searchIndex)
                return ret

        

        