class Solution:

    import re

    def isPalindrome(self, s: str) -> bool:
    
        s = re.sub(r'[^a-zA-Z0-9]', "", s.lower())
        start = 0
        end = len(s) - 1

        while start < end:

            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
