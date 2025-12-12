def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    s = str(x)
    
    return s == s[::-1]

# --- Examples ---

# Example 1
x1 = 121
output1 = isPalindrome(x1)
print("Example1: ")
print(f"Input: x = {x1}")
print(f"Output: {output1}")


# Example 2
x2 = -121
output2 = isPalindrome(x2)
print("Example2: ")
print(f"Input: x = {x2}")
print(f"Output: {output2}")
