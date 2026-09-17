class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        square_map = defaultdict(list)
        
        for i in range(0, 9):
            for j in range(0, 9):

                if board[i][j] == '.':
                    continue

                if (board[i][j] in row_map[i] 
                or board[i][j] in col_map[j] 
                or board[i][j] in square_map[(i//3, j//3)]):
                    return False

                row_map[i].append(board[i][j])
                col_map[j].append(board[i][j])
                square_map[(i//3, j//3)].append(board[i][j])

        return True

            
