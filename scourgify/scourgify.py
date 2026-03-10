import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
    sys.exit("Invalid File")

try:
    with open(sys.argv[1]) as file, open(sys.argv[2], "w") as file1:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(file1, fieldnames = ["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first" : first, "last" : last, "house" : row["house"]})


except FileNotFoundError:
    sys.exit("Unable to open the file")
