class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = dict(('()', '[]', '{}'))

        my_stack = []

        for p in s:
            if p in '([{':
                my_stack.append(p)
            elif len(my_stack) == 0 or p != paren_dict[my_stack.pop()]:
                return False
                
        return len(my_stack) == 0