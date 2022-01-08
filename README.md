# Election Analysis (Module)
## Project Overview 
We helped the Colorado Board of Elections complete an analysis of a recent congressional election.  In this audit we:
- Calculated the total number of votes.
- Got a complete list of candidates who recived votes.
- Calculated the total number of votes each candidate received. 
- Calculated the percentage of votes each candidate won.
- Determined the winner of the election based on popular vote. 
## Resources
- Data Source: election_results.csv
Software: Python 3.7.6, Visual Studio Code 
## Summary
##### Total Number of Votes Cast
369,711 votes
##### Candidates
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane
##### Candadate Results 
- Charles Casper Stockham 
    - Won 23.0% of the vote 
    - 85,213 votes
- Diane DeGette 
    - Won 73.8% of the vote
    - 272,892 votes
- Raymond Anthony Doane
    - Won 3.1% of the vote
    - 11,606 votes

## Results 
Diane DeGette by winning 73.8% with 272,892 votes out of 369,711 total votes!

# Election Audit (Challenge)
## Overview
After delivering our analysis to the Colorado Board of Elections, they asked us to audit the analysis to include the individual count votes.  The Board of Elections wanted to know, how many votes each county casted and what percentage of the total vote they held in order to determine which county had the largest turnout.  
## Election Audit Results 
- **369,711 total votes** cast in the congressional election.
- **County Vote Results:**
  - Jefferson: 38,855 votes (10.5%)
  - Denver: 306,055 votes (82.8%)
  - Arapahoe" 24,801 votes (6.7%)
- **Denver** was the county with the largest vote turnout.
- **Candidate Vote Results:**
  - Charles Casper Stockham: 85,213 votes (23.0%)
  - Diana DeGette: 272,892 votes (73.8%)
  - Raymon Anthony Doane: 11,606 votes (3.1%)
- **Election Results:**
  - Winner: **Diana DeGette**
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%
## Election Audit Summary
While this script was commissioned for the most recent election, it can be repurposed to audit future elections as well.  The script itsself is written to pull data from and save information to two individual files, not just the two we used in this analysis.  Thus, as long as you have two files, one CSV with data in the same format as this one, and a blank text file to save information to, the script can easily be altered to run the same analysis on new data.  In order to do so, I reccomend making the following alerations:
1. Import a new CSV file with the respective election's data in the same format as before and save it under a more specific name, preferably using the year within the title.  
   - Replace the current document's name with the new one in lines 9, 34, and 35.  
   - This will import and open to read the new file's data instead of the current one we used in this analysis. 
2. Create a new text file to save your results to- and save it under a more specifc name as you did in reccomendation #1 above. 
   - Replace the current document's name with the new one in lines 93, 125, 140 and 158.
   - This will save your new results into your new text file instead of the one we used in this election. 

  
