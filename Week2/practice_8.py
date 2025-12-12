def moveZeros(nums):
    insert_pos = 0
    # First pass: move all non-zero elements to the beginning of the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1      
    # Second pass: fill the remaining positions with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
# Example usage:
nums_example = [0, 1, 0, 3, 12]
moveZeros(nums_example)
print("Example1: ",nums_example) 
#Example 2:
nums_example =[0]
moveZeros(nums_example)
print("Example2: ", nums_example)
