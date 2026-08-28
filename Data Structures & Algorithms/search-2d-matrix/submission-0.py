class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Run BS on rows (between start and end) and then cols


        #Find Row:
        hiRow, loRow = len(matrix) - 1, 0
        useRow = 0

        # Works, we are selecting the correct row
        while loRow <= hiRow:
            midRow = (hiRow + loRow) // 2
            startMid, endMid = matrix[midRow][0], matrix[midRow][len(matrix[midRow]) - 1]
            if target < startMid:
                hiRow = midRow - 1
            elif target > endMid:
                loRow = midRow + 1
            else:
                useRow = midRow
                break
        
        hi, lo = len(matrix[useRow]) - 1, 0
        while lo <= hi:
            mid = (hi + lo) // 2
            
            if target < matrix[useRow][mid]:
                hi = mid - 1
            elif target > matrix[useRow][mid]:
                lo = mid + 1
            else:
                return True

        return False
