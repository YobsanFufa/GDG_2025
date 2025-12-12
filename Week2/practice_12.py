total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        try:
            num = int(line.strip())
            total += num
        except ValueError:
            continue  # skip invalid lines

print("Sum =", total)
