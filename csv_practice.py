import csv
print("--- EXERCISE 1: Setup")
csv_file_path = '/home/hai_dang_phung/ism2411-lab12/data/sales.csv'
print("\n--- EXERCISE 2: Read and print raw rows ---")
with open(csv_file_path, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)