import os
import csv

csvpath = os.path.join("/Users/aleksandrakrysiuk/Desktop/Python-Challenge-3/PyPoll/Resources/election_data.csv")

total_cast = 0
candidates_received_votes = set()
how_many = "Raymon Anthony Doane"
count_Raymon = 0
how_many2 = "Diana DeGette"
count_Diana = 0
how_many3 = "Charles Casper Stockham"
count_Charles = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        total_cast += 1
        name = row[2]
        candidates_received_votes.add(name)


        if row[2] == how_many:
            count_Raymon += 1
        if row[2] == how_many2:
            count_Diana += 1
        if row[2] == how_many3:
            count_Charles += 1


Raymon_perc = (count_Raymon/ total_cast) * 100
Diana_perc = (count_Diana/total_cast) * 100
Charles_perc = (count_Charles/total_cast) *100

largest_number=max(count_Charles,count_Diana,count_Raymon)

print ("Election Results")
print("----------------------------")
print("Total Votes:", total_cast)
print("----------------------------")
print(f"{how_many3}: {count_Charles / total_cast * 100:.3f}% ({count_Charles})")
print(f"{how_many2}: {count_Diana / total_cast * 100:.3f}% ({count_Diana})")
print(f"{how_many}: {count_Raymon / total_cast * 100:.3f}% ({count_Raymon})")
print("----------------------------")

if largest_number == count_Charles:
    print("Winner: Charles Casper Stockham")
elif largest_number == count_Diana:
    print("Winner: Diana DeGette")
else:
    print("Winner: Raymon Anthony Doane")

print("----------------------------")