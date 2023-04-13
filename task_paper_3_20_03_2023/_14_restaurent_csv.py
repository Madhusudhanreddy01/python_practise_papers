'''14. Write a command-line program which helps a traveler keep track of the
restaurants they've visited in different cities and what they thought of each. The
program will accept two CSV files of restaurants, a "primary list" CSV and a
"sublist" one, and update the primary one with new restaurants from the trip one.'''

import csv

fields = ["Place","Food","price(per plate)","ratings(out of 10)"]

rows = [["Hyderabad","Chicken-Biryani","200","8"],
        ["Bangalore","Bisi bele bath","100","9"],
        ["Chennai","Idly-sambar","50","9"],
        ["Mumbai","Vada-pav","20","8"]
        ]

filename = "record.csv"

with open(filename,"w+" ) as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    
    csvfile.seek(0)
    csvreader = csv.reader(csvfile)
    liss = list(csvreader)
    print(liss)
    for lines in liss:
        if lines:
            print("  ".join(lines))