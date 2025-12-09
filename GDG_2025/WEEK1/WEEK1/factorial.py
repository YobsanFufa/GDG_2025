def factorial(i):
    if i< 0:
        return "Factorial is not defined"
    if i == 0:
        return 1
    if i > 0:
        fact = 1
        for n in range(1, i+1):
            fact *= n
        return fact
    else:
        return "YOU ENTERED WRONGLY."
Number = int(input("Enter Factorial Number: "))
result = factorial(Number)
print(f"The factorial of {Number}  is: {result}")