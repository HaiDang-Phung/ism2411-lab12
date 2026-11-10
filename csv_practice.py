"""
Reflection Questions:
1. You've now completed a full ETL pipeline: read a CSV, transform the data, write a new CSV. How does this compare to doing the same task in Excel? What can Python do that Excel can't do easily, and vice versa?
   - Building an ETL pipeline in Python offers unmatched automation, repeatability, 
and scalability for processing large datasets compared to manual workflows in Excel. 
Python excels at handling thousands of files automatically, executing complex data transformations, 
and integrating smoothly with web APIs or databases, whereas Excel provides an intuitive graphical interface 
ideal for quick ad-hoc analysis and visual formatting.

2. Exercise 8 showed you append mode. Think of a real business process that would benefit from an append-mode log file — describe it and explain why append mode is the right tool.
   - An e-commerce transaction logging or server activity monitoring system is an ideal use case. 
Append mode is the correct tool because it allows the system to continuously record new chronological events 
as they occur without overwriting or destroying historical log data.
"""
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
print("\n--- EXERCISE 7: Sales summary by product ---")
product_summary = {}
with open(csv_file_path, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if product in product_summary:
            product_summary[product] += line_total
        else:
            product_summary[product] = line_total
sorted_summary = sorted(product_summary.items())
for prod, rev in sorted_summary:
    print(f"{prod}: ${rev:.2f}")
print("\n--- EXERCISE 8: Append mode log ---")
from datetime import datetime
log_file_path = "/home/hai_dang_phung/ism2411-lab12/data/run_log.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_file_path, mode="a", encoding="utf-8") as logfile:
    logfile.write(f"{timestamp} | Total Revenue: ${total_revenue_all:.2f}\n")
print(f"Logged run at {timestamp} to {log_file_path}")