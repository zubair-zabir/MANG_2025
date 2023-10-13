class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_maps = {
            ")": "(", "}": "{", "]":"["
        }
        opening_bracket = set(["(","{","["])
        for c in s:
            if c in opening_bracket:
                stack.append(c)
            elif stack and stack[-1] == bracket_maps[c]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True

        
