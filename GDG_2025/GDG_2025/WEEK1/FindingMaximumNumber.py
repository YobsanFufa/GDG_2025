def find_maximum(a):
    return max(a)
user_input = input("Enter numbers separated by space: ")
Numbers = list(map(int, user_input.split()))
result = find_maximum(Numbers)
print("Maximum Number is:", result)
