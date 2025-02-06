#git sync

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Store the original number to compare later
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10  # Get the last digit
            reversed_num = reversed_num * 10 + digit  # Build reversed number
            x //= 10  # Remove the last digit
        
        return original == reversed_num
        