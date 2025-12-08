def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    if  b != 0:
        return "Invalid"
    return a/b
def multi(a,b):
    return a*b
  
Num1 = float(input("Enter First Number: "))
Num2 = float(input("Enter Second Number: "))
operator = input("Enter Operator :+ ,- , / , *")
if operator == "+":
    result = add(Num1, Num2)

elif operator == "-":
    result = sub(Num1, Num2)
elif operator =="/":
    result = div(Num1, Num2)
elif operator =="*":
    result = multi(Num1, Num2)
else:
    print("invalid operation")
print("Result: ", result)