bool isPalindrome(int x) {
    // Negative numbers are not palindromes
    if (x < 0) return false;
    
    // Store the original number
    int original = x, reversed = 0;
    
    while (x > 0) {
        int digit = x % 10;  // Extract last digit
        if (reversed > (2147483647 - digit) / 10) return false; // Prevent overflow
        reversed = reversed * 10 + digit; // Build reversed number
        x /= 10;  // Remove last digit
    }
    
    return original == reversed;
}