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
