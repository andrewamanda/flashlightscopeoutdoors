import csv
import sys

def process_csv(input_file, output_file):
    with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['Merged']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            merged = f"{row['Company Name']}\nAttn: {row['Executive First Name']} {row['Executive Last Name']}\n{row['Address']}\n{row['City']}, {row['State']} {row['ZIP Code']}"
            writer.writerow({'Merged': merged})

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python merge_csv.py input_file.csv output_file.csv")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_csv(input_file, output_file)
