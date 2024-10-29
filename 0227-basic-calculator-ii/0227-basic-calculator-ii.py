class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operation = '+'  # Initialize the operation to '+'
        
        for i, char in enumerate(s):
            # Build the current number if it's a digit
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # If char is an operator or it's the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    # Integer division, handling towards zero
                    top = stack.pop()
                    stack.append(int(top / current_num))
                
                # Reset current_num and update operation
                current_num = 0
                operation = char
        
        # Sum up all values in the stack for the result
        return sum(stack)

