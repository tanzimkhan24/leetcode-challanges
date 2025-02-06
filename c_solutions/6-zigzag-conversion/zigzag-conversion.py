# git sync

class Solution:
    def convert(self, s: str, numRows: int) -> str:
         # Edge case: If there is only one row, return the string as is
        if numRows == 1 or numRows >= len(s):
            return s
    
        # Create a list of empty strings for each row
        rows = ["" for _ in range(numRows)]
    
        # Variables to track the current row and direction
        current_row = 0
        going_down = False
    
        # Loop through each character in the input string
        for char in s:
            rows[current_row] += char  # Append the character to current row
        
            # Reverse direction when reaching the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
        
            # Move up or down depending on the current direction
            current_row += 1 if going_down else -1
    
        # Join all rows to form the final zigzag string
        return "".join(rows)

        