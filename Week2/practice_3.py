with open("log.txt", "a") as file:
    file.write("user Logged in\n")
with open("log.txt", "r") as file:
    history = file.read()
print("Full Log History: ")
print(history)

