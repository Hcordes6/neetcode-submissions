class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # run BS on rows, then cols within selected row range

        lo, hi = 0, len(matrix) - 1
        selectedRow = 0

        #select row
        while(lo <= hi):
            mid = (hi + lo) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                selectedRow = mid
                break
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        lo, hi = 0, len(matrix[selectedRow]) - 1

        while lo <= hi:
            mid = (hi + lo) // 2

            if matrix[selectedRow][mid] == target:
                return True
            elif matrix[selectedRow][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        
        return False

