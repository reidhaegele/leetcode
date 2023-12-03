class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squ = {}
        rc = 0
        row = {}
        for y in board:
            col = {}
            cc = 0
            for x in y:
                if x != '.':
                    if squ.get(x + str(cc // 3) + str(rc // 3), -1) > 0:
                        return False
                    squ[x + str(cc // 3) + str(rc // 3)] = squ.get(x + str(cc // 3) + str(rc // 3), 0) + 1
                    if row.get(x + str(cc), -1) > 0:
                        return False
                    row[x + str(cc)] = row.get(x + str(cc), 0) + 1
                    if col.get(x, -1) > 0:
                        return False
                    col[x] = col.get(x, 0) + 1
                cc += 1
            rc += 1
        return True