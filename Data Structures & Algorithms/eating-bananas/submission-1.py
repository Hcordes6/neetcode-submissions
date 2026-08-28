class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # basically do tests runs of Koko eating the bananas at different rates
        # where the rate is determined by the mid of the current Binary search from 1 to m
        # where m is the largest value in the pile

        #first, find largest
        largest = 0
        for i in piles:
            largest = max(largest, i)
        
        # Then, init BS where mid runs through the eating process. 
        # O(nlogm) time

        hi, lo = largest, 1
        currBest = largest
        while lo <= hi:
            mid = (hi + lo) // 2

            # eating process:
            tempHrs = h
            for pile in piles:
                tempHrs -= math.ceil(pile / mid)
            
            if tempHrs < 0:
                lo = mid + 1
                
                # minimize number as close to 0 as possbile, does not necessarily need to be 0
            elif tempHrs >= 0:
                currBest = min(mid, currBest)
                hi = mid - 1
        return currBest