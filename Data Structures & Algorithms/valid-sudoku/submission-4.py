class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # add index of number instance to the value of the number key,
        # compare indicies to each instance, 
        # if not equal, add to values
        # Must catch "."

        # NOTE: Must be separate for i and j to avoid mismatch
        hashmapi = {}
        hashmapj = {}
        grid = {}
        for i in range(len(board)):
            print(f"row: {i}")
            boxRow = math.floor(i / 3)
            for j in range(len(board[i])):
                # catch "."
                print(f"col: {j}")
                if board[i][j] == ".":
                    continue
                # do the 3x3 grid checks
                boxCol = math.floor(j / 3)
                boxCoord = [boxRow, boxCol]
                if board[i][j] in grid:
                    currentValuesList = grid[board[i][j]]
                    for k in range(1, len(currentValuesList), 2):
                        if boxRow == currentValuesList[k-1] and boxCol == currentValuesList[k]:
                            print(f"    {boxRow} = {currentValuesList[k-1]}; {boxCol} = {currentValuesList[k]}")
                            return False
                        else:
                            currentValuesList.append(boxRow)
                            currentValuesList.append(boxCol)
                            grid.update({board[i][j] : currentValuesList})
                else:
                    grid.update({board[i][j] : boxCoord})
                 # hashmaps will always be the same length w the same keys
                if board[i][j] not in hashmapi:
                    hashmapi.update({board[i][j] : [i + 1]})
                    hashmapj.update({board[i][j] : [j + 1]})
                # Check if values equal current indicies
                else: 
                    currentValuesi = hashmapi[board[i][j]]
                    currentValuesj = hashmapj[board[i][j]]
                    print(f"{currentValuesi} at {i}, {j}")
                    for value in currentValuesi:
                        if value == i + 1:
                            return False
                    for value in currentValuesj:
                        if value == j + 1:
                            return False
                    # add current indicies to values
                    currentValuesi.append(i + 1)
                    currentValuesj.append(j + 1)
                    hashmapi.update({board[i][j] : currentValuesi})
                    hashmapj.update({board[i][j] : currentValuesj})
            

        return True