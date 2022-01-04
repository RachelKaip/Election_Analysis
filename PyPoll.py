import csv
import os
file_to_load= os.path.join("Resources", "election_results.csv")
file_to_save= os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)  
    
    #To-do: Read and analyze data here
    #read and print header row 
    headers = next(file_reader)
    print(headers)
    
    
   
election_data.close()









#Data we need to retrieve:
#1. total number of votes cast
#2. A complete list of candidates who recived votes
#3. The percetage of votes each candidates won 
#4. Total number of votes a candidate won
#5. The winner of the election based on popular vote 



