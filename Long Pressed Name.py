class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
    
        while j < len(typed):
            # If characters match, move both pointers.
            if i < len(name) and name[i] == typed[j]:
                i += 1
        # If characters don't match and it's not a repetition of the previous character in typed, return False.
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        # If it's a repetition, just move the typed pointer.
            j += 1
    
    # Ensure we've processed all characters in the name.
        return i == len(name)
