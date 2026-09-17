class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr = 0
        rr = len(matrix) - 1

        while lr <= rr:
            mr = lr + (rr-lr) // 2

            if target > matrix[mr][-1]:
                lr = mr + 1
            elif target < matrix[mr][0]:
                rr = mr - 1
            else:
                break

        lc = 0
        rc = len(matrix[0])-1

        while lc <= rc:
            mc = lc + (rc-lc) // 2

            if target > matrix[mr][mc]:
                lc = mc + 1
            elif target < matrix[mr][mc]:
                rc = mc - 1
            else:
                return True
        return False
            