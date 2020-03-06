# __main__.py
# list the sheets 

import sys, openpyxl, csv
import os

if len(sys.argv) < 2:
    print("Need to provide a file-path to the xlsx file.")
    exit()

file_path = sys.argv[1]
if not os.path.exists(file_path):
    print(f"No file at [{file_path}]")
    exit()

print(f"Converting [{file_path}] to csv.")
workbook = openpyxl.load_workbook(file_path)
for worksheet in workbook:
    csv_file_path = f"{worksheet.title}.csv" 
    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in worksheet.rows:
            writer.writerow([cell.value for cell in row])