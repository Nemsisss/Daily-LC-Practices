class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
     # iterate through all rows:
        for arr in board:
            for item in arr:
                if arr.count(item)>1 and item!=".":
                    return False
    #iterate through all columns:
        for col in range(0,9):
            colArr=[]
            for row in range(0,9):
                if board[row][col]!=".":
                    if board[row][col] in colArr:
                        return False
                    colArr.append(board[row][col])
                
    #iterate through all 3x3 squares:
        squareArr=[]
        for counter in range (0,7,3):
            for row in range(0, 9):
                if row%3==0:
                    squareArr=[]
                for col in range(counter, counter+3):
                    if board[row][col]!=".":
                        if board[row][col] in squareArr:
                            return False
                        squareArr.append(board[row][col])
    
        return True
