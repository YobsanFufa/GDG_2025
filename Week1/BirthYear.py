def Birthday(age, currentyear):
    return currentyear-age


age = int(input("Enter your age: "))
currentyear = int(input("Enter Current Year: "))
result = Birthday(age, currentyear)
print("Your Birth Year is : ", result)
