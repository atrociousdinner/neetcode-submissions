class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       lr = 0
       rr = len(matrix)-1
       row = []

       while lr <= rr:
        mr = lr + (rr-lr)//2

        if target > matrix[mr][-1]:
            lr = mr+1
        elif target < matrix[mr][0]:
            rr = mr-1
        else:
            row = matrix[mr]
            break

       if not row:
        return False

       lc = 0
       rc = len(row)-1

       while lc <= rc:
            mc = lc + (rc-lc)//2
            if target < row[mc]:
                rc = mc - 1
            elif target > row[mc]:
                lc = mc + 1
            else:
                return True 
       return False