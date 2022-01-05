# add our dependancies 
import csv
import os
# Assign a variable to load a file from a path.
file_to_load= os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save= os.path.join("analysis", "election_analysis.txt")

#initilalizze variable called total_votes to 0 
total_votes=0

#declare a list to store candidate names 
candidate_options= []

#declare empty dictionary for candidate votes
candidate_votes={}

#declare empty string variable that holds winning candidate
winning_candidate= ""

#declare winning count and set to 0
winning_count= 0

#declare winning percentage and set to 0
winning_percentage= 0

#open the election results file and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)  

    #read and print header row 
    headers = next(file_reader)
   
    #print each row in csv file
    for row in file_reader:
        #after iterrating through the rows, add the total votes (total_votes = total_votes+1)
        total_votes+=1
        #print the candidate name from each row 
        candidate_name = row[2] 
        #add candidate name inot dict once 
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #start tracking the candidate's vote count, setting each cand's votes to 0 
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1
#iterate through the candidate votes  
for candidate_name in candidate_votes:
    #get the votes for each candidate
    votes = candidate_votes[candidate_name]
    #calc percent of votes
    vote_percentage = float(votes)/float(total_votes)*100
    #print candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    #determine the winner based on vote count and %
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage 
        winning_candidate= candidate_name

    #to do: print cand's names, vote counts, and % votes 
    print(f"{candidate_name} : {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n")

print(winning_candidate_summary)




    
   










#Data we need to retrieve:
#1. total number of votes cast
#2. A complete list of candidates who recived votes
#3. The percetage of votes each candidates won 
#4. Total number of votes a candidate won
#5. The winner of the election based on popular vote 



