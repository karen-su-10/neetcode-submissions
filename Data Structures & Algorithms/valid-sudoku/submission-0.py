class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rule 1 and construct new column array
        #intial with values ,not empty array
        column_array = [["."] * 9 for _ in range(9)]
        for r in range(0,9):
            dupset = set()
            # exclusive list
            for c in range(0,9):
                cell = board[r][c]
                column_array[c][r]=cell
                if cell != ".":
                    if cell in dupset:
                        return False
                    dupset.add(cell)
        #check rule 2
        for r in range(0,9):
            dupcol = set()
            for c in range(0,9):
                cell = column_array[r][c]
                if cell != ".":
                    if cell in dupcol:
                        return False
                    dupcol.add(cell)
        #check rule 3
        #construct subarrays
        subarrays = []
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                subarray = []
                for r in range(row, row + 3):
                    subarray.append(board[r][col:col + 3])
                subarrays.append(subarray)
        #for each subarrray, use function checkdup to check
        def isValidSubArray(subArray:List[List[str]]) -> bool:
            subset = set()
            for r in range(0, len(subArray)):
                for c in range(0, len(subArray[0])):
                    cell = subArray[r][c]
                    if cell != ".":
                        if cell in subset:
                            return False
                        subset.add(cell)
            return True
        
        for subarray in subarrays:
            result = isValidSubArray(subarray)
            if result == False:
                return False
        
        return True
