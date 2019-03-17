# election_data.py

''' Description:
  This script will be used to modernize its vote-counting process of a 
  small town.

  Given a set of poll data called (./Resources/election_data.csv). 
  The dataset is composed of three columns: `Voter ID`, `County`, and 
  `Candidate`. 
  
  This script will analyze the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  
'''
import csv

# Open the CSV file and read the data into a dictionary (bd)
# bd will hold a list of the dictionaries read

with open('./Resources/election_data.csv') as csvfile:
    elec_data = list(csv.DictReader(csvfile))
    
khan_tot = 0
correy_tot = 0
li_tot = 0
otooley_tot = 0
most_votes = 0
total_votes = len(elec_data)


for i in range(total_votes):
    if(elec_data[i]['Candidate'] == 'Khan'):
        khan_tot += 1
    if(elec_data[i]['Candidate'] == 'Correy'):
        correy_tot += 1
    if(elec_data[i]['Candidate'] == 'Li'):
        li_tot += 1
    if(elec_data[i]['Candidate'] == "O'Tooley"):
        otooley_tot += 1


    
if correy_tot > most_votes:
    most_votes = correy_tot
    winner = 'Correy'
    
if li_tot > most_votes:
    most_votes = li_tot
    winner = 'Li'
    
if khan_tot > most_votes:
    most_votes = khan_tot
    winner = 'Khan'
    
if otooley_tot > most_votes:
    most_votes = otooley_tot
    winner = "O'Tooley"
    
print("Election Results")
print("-------------------------------------")
print("Total Votes: ", total_votes)
print("-------------------------------------")

print("Khan: " +  "{:.{}f}%".format(khan_tot/total_votes *100,2) , "(", khan_tot, ")" + " of the vote" )
print("Correy: " +  "{:.{}f}%".format(correy_tot/total_votes *100,2) , "(", correy_tot, ")" + " of the vote" )
print("Li: " +  "{:.{}f}%".format(li_tot/total_votes *100,2) , "(", li_tot, ")" + " of the vote" )
print("O'Tooley: " +  "{:.{}f}%".format(otooley_tot/total_votes *100,2) , "(", otooley_tot, ")" + " of the vote" )

print("--------------------------------------")
print("The Winner is: ", winner, " with ", most_votes, " votes")
print("--------------------------------------")

reportFile = open('./election_results.txt', "w")
reportFile.write("Election Results\n")
reportFile.write("-------------------------------------\n")
reportFile.write("Total Votes: " + str(total_votes) + " \n")
reportFile.write("-------------------------------------\n")

reportFile.write("Khan: " +  "{:.{}f}%".format(khan_tot/total_votes *100,2) + " (" + str(khan_tot) + ")" + " of the vote\n" )
reportFile.write("Correy: " +  "{:.{}f}%".format(correy_tot/total_votes *100,2) + " (" + str(correy_tot) + ")" + " of the vote\n" )
reportFile.write("Li: " +  "{:.{}f}%".format(li_tot/total_votes *100,2) + " (" + str(li_tot) + ")" + " of the vote\n" )
reportFile.write("O'Tooley: " +  "{:.{}f}%".format(otooley_tot/total_votes *100,2) + " (" + str(otooley_tot) + ")" + " of the vote\n" )

reportFile.write("--------------------------------------\n")
reportFile.write("The Winner is: " + str(winner) + " with " + str(most_votes) + " votes\n")
reportFile.write("--------------------------------------\n")

reportFile.close()

    

