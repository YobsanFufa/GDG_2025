def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {} 

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return [] 


# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = twoSum(nums1, target1)
print("Example1: ")
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {result1}")


# Example 2
nums2 = [3, 2, 4]
target2 = 6
result2 = twoSum(nums2, target2)
print("Example2: ")
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {result2}")