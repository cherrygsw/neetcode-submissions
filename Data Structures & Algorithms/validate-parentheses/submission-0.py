class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:  
                topElement = stack.pop() if stack else "#"
                if mapping[char] != topElement:
                    return False
            else:  # if it's an opening bracket
                stack.append(char)

        return not stack
