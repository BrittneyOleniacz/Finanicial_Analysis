
import os
import csv

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
oTooley_votes= 0

path = "election_data.csv"
with open(path) as election_data:
	csvreader = csv.DictReader(election_data)
	for row in csvreader:
		total_votes = total_votes + 1
		if row["Candidate"]	== "Khan":
			khan_votes = khan_votes + 1
		if row["Candidate"] == "Correy":
			correy_votes = correy_votes + 1
		if row["Candidate"] ==	"Li":
			li_votes =	li_votes + 1
		if row["Candidate"] == "O\'Tooley":
			oTooley_votes = oTooley_votes + 1
  	
per_kahn = khan_votes/total_votes * 100
per_correy = correy_votes/total_votes * 100
per_li = li_votes/total_votes * 100
per_oTooley = oTooley_votes/total_votes * 100
 
if oTooley_votes > li_votes and oTooley_votes > correy_votes and oTooley_votes > khan_votes:
	winner = "O\'Tooley"
if li_votes > correy_votes and li_votes > khan_votes and li_votes > oTooley_votes:
	winner = "Li"
if correy_votes > khan_votes and correy_votes > oTooley_votes and correy_votes > li_votes:
    winner = "Correy"
if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > oTooley_votes:
    winner = "Khan"
  
output = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {per_kahn:.3f}% {khan_votes}
Correy: {per_correy:.3f}% ({correy_votes})
Li: {per_li:.3f}% ({li_votes})
O'Tooley: {per_oTooley:.3f}% ({oTooley_votes})
-------------------------
Winner: {winner}
-------------------------
'''
print(output)
output_file = os.path.join("PyPollResults.txt")
with open(output_file, 'w') as textfile:
    textfile.write(output)
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#					Sources
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# https://stackoverflow.com/questions/39521096/how-to-add-apostrophes-in-a-dictionnary
# https://docs.python.org/3/library/csv.html
# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
# https://www.geeksforgeeks.org/float-in-python/
# https://www.learnpython.org/en/Basic_Operators
# https://www.python.org/dev/peps/pep-0498/
# Supplemental/Python_Reference_Guide.pdf
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

