
valid_sales = []
with open("sales.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        clean_line = line.strip() 

        try:
        
            sale = int(clean_line)
            valid_sales.append(sale)  
        except ValueError:
            print(f"Skipping invalid line {line_number}: '{clean_line}'")
total_sales = sum(valid_sales)
print("\nValid sales numbers:", valid_sales)
print("Total sales:", total_sales)