class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last = s.rfind(' ') + 1
        print(last)
        print(len(s[last:]))
        return len(s[last:])


if __name__ == "__main__":
        s = Solution()
        
        print(s.lengthOfLastWord("Hello World"))
        print(s.lengthOfLastWord("Hello World                "))
        print(s.lengthOfLastWord("      Hello     World    "))