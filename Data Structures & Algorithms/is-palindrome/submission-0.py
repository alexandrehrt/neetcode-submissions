import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = re.sub(r'[^a-zA-Z0-9]', '', s)

        left, right = 0, len(cleanString) -1
        
        while left < right:
            if (cleanString[left]).lower() != cleanString[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

        