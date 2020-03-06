# __main__.py

import sys, openpyxl, csv, os, argparse

parser = argparse.ArgumentParser(prog="xlsx2csv")
parser.add_argument("file_path", help="file-path of xlsx file to convert.")
parser.add_argument("-s", "--sheets", nargs='*', default=None, help="names of worksheets to convert.")

args = parser.parse_args(sys.argv[1:])

file_path = args.file_path
if not os.path.exists(file_path):
    print(f"No file located at [{file_path}].")
    exit()

workbook = openpyxl.load_workbook(file_path)

if args.sheets:
    worksheet_names = args.sheets
else:
    worksheet_names = workbook.sheetnames

print(f"Converting [{file_path}] to csv...")
for worksheet_name in worksheet_names:
    worksheet = workbook[worksheet_name]
    csv_file_path = f"{worksheet.title}.csv"
    print(f"Exporting sheet [{worksheet_name}] to [{csv_file_path}].")
    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in worksheet.rows:
            writer.writerow([cell.value for cell in row])