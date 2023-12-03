class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "")
        st = st.lower()
        
        left = 0
        right = len(st) - 1
        while left <= right:
            if (ord(st[left]) >= ord('a') and ord(st[left]) <= ord('z')) or ((ord(st[left]) >= ord('0') and ord(st[left]) <= ord('9'))):
                pass
            else:
                left += 1
                continue
            if (ord(st[right]) >= ord('a') and ord(st[right]) <= ord('z')) or ((ord(st[right]) >= ord('0') and ord(st[right]) <= ord('9'))):
                pass
            else:
                right -= 1
                continue
            if st[left] != st[right]:
                return False
            right -= 1
            left += 1
        return True