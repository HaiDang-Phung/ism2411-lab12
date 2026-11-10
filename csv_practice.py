import csv
print("--- EXERCISE 1: Setup")
csv_file_path = '/home/hai_dang_phung/ism2411-lab12/data/sales.csv'
print("\n--- EXERCISE 2: Read and print raw rows ---")
with open(csv_file_path, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print("\n--- EXERCISE 3: Skip the header ---")
with open(csv_file_path, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    print("Data rows:")
    for row in reader:
        print(row)
print("\n--- EXERCISE 4: Compute totals ---")
total_revenue_all = 0.0
with open(csv_file_path, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue_all += line_total
        print(f"{product}: {quantity} units x ${price:.2f} = ${line_total:.2f}")
print(f"Overall Total Revenue: ${total_revenue_all:.2f}")
print("\n--- EXERCISE 5: Filter and write ---")
cleaned_file_path = "/home/hai_dang_phung/ism2411-lab12/data/cleaned.csv"
total_rows = 0
qualifying_rows = 0
with open(csv_file_path, mode="r", encoding="utf-8") as infile, \
     open(cleaned_file_path, mode="w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        total_rows += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([product, price, quantity, f"{line_total:.2f}"])
            qualifying_rows += 1
print(f"Total rows in original: {total_rows}")
print(f"Qualifying rows written to cleaned.csv: {qualifying_rows}")
print("\n--- EXERCISE 6: csv.DictReader ---")
total_revenue_dict = 0.0
with open(csv_file_path, mode="r", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        total_revenue_dict += line_total
print(f"Total revenue calculated using DictReader: ${total_revenue_dict:.2f}")
# Comparison:
# Use csv.reader for high-performance reading when column order is strictly fixed and known by index positions.
# Use csv.DictReader when code readability, maintainability, and column name-based access are needed to prevent errors if column orders shift.