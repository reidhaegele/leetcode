class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)


        if(len(s)!=len(t)): return False
        countS, countT = {}, {}
        for x in range(len(s)):
                countS[s[x]] = 1 + countS.get(s[x], 0)
                countT[t[x]] = 1 + countT.get(t[x], 0)
        for c in countS:
                if(countS[c]!=countT.get(c,0)):
                        return False 
        return True

        # if(len(s)!=len(t)): return False
        # i = 0
        # while (i < len(s)):
        #     if(t.find(s[i]) != -1):
        #         t = t.replace(s[i], '', 1)
        #         s = s.replace(s[i], '', 1)
        #         i-=1
        #     i += 1
        # return len(t) == 0


if __name__ == "__main__":
    s = Solution()

    print(s.isAnagram("car", "rac"))
    print(s.isAnagram("car", "top"))
    print(s.isAnagram("car", "cat"))
    print(s.isAnagram("ab", "a"))
    print(s.isAnagram("racecar", "racecar"))
