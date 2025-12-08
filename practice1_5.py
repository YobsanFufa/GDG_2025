
total_sales = 0
invalid_lines = []

with open("sales.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        clean_line = line.strip()
        try:
            amount = float(clean_line)
            total_sales += amount
        except ValueError:
            invalid_lines.append((line_number, clean_line))

print("Total of valid sales:", total_sales)
if invalid_lines:
    print("\nInvalid entries found:")
    for num, value in invalid_lines:
        print(f"Line {num}: '{value}'")