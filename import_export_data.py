import csv

data_to_export = [
    ['Name', 'Age', 'Department'],
    ['Alice', 28, 'Engineering'],
    ['Bob', 34, 'Marketing'],
    ['Charlie', 25, 'Design']
]

filename = 'employee_data.csv'

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_export)
print(f"Data successfully exported to '{filename}'\n")

imported_data = []

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        imported_data.append(row)

print("Data imported from file:")
for row in imported_data:
    print(row)
