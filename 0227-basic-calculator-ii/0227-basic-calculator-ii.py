class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        curr = 0
        prev = 0
        res = 0
        cur_operation = '+'
        
        while i < len(s):
            cur_char = s[i]
            
            # If the character is a digit, construct the full number
            if cur_char.isdigit():
                curr = 0  # Reset curr for the new number
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1  # Adjust index since outer loop will increment it
                
                # Perform the previous operation
                if cur_operation == '+':
                    res += curr
                    prev = curr
                elif cur_operation == '-':
                    res -= curr
                    prev = -curr
                elif cur_operation == '*':
                    res -= prev  # Remove last added number
                    prev = prev * curr  # Update prev for multiplication
                    res += prev  # Add the result of multiplication
                elif cur_operation == '/':
                    res -= prev  # Remove last added number
                    prev = int(prev / curr)  # Update prev for division
                    res += prev  # Add the result of division
                
                curr = 0  # Reset curr after processing the number
            
            elif cur_char != " ":
                cur_operation = cur_char  # Update the operation for next number
            
            i += 1
        
        return res
