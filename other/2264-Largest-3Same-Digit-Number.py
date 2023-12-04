class Solution:
    def largestGoodInteger(self, num: str) -> str:
        trios = []
        for i in range(len(num) - 2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                trios.append(int(num[i] + num[i+1] + num[i+2]))
        if not trios:
            return ""
        res = str(max(trios))
        if res == "0":
            res = res * 3
        return res