import csv

csv_file = open("data/all.txt", "r", encoding="utf_8")

f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in f:
    print(row[0] + "," + row[1] + "," + row[2] + "," + row[3])
