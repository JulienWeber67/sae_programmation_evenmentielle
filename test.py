import csv

with open('testing.csv', 'w', newline='') as csvfile:
    fieldnames = ['port', 'machine']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'port': input('port :'), 'machine': input('machine :')})
    writer.writerow({'port': input('port :'), 'machine': input('machine :')})
    writer.writerow({'port': input('port :'), 'machine': input('machine :')})

with open('testing.csv', newline='') as csvfile:
    fieldnames = ['port', 'machine']
    reader = csv.DictReader(csvfile)

    for row in reader:

        print(row['port'], row['machine'])
