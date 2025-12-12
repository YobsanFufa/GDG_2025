try:
    with open("message.txt", "r") as file:
        content = file.read()
        print(content.upper())
except FileNotFoundError:
    print("File not found!")
