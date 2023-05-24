class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        numToString = str(x)

        if numToString == numToString[::-1]:
             return True
        else:
            return False

