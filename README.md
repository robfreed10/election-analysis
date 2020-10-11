# Election_Analysis
using Python to analyze election results in Colorado 

## Project Overview
A Colorado Board of Elections employee has tasked me the following for the audit of a local congressional election. 
  1. Calculate total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on the popular vote. 

## Resources
Data Source: election_results.csv (resources folder)
Software: Python 3.7 

## Challenge Overview
The purpose of this audit was to determine which candidate was the winner of the popular vote as well as which county had the most voters as well as the percentages of votes for the 3 counties in the election: Arapahoe, Denver, and Jefferson. This audit will give a better understanding to future candidates so that when the next election comes around, they will campaign more or less in certain counties. 

## Election Audit Results by County
This election audit brought about significant results for the counties involved in this congressional election. 
 
      - There were 369,711 votes in this congressional election
      - Jefferson County had 10.5% (38,855 of 369,711) of total popular vote
      - Denver County had 82.8% (306,055 of 369,711) of total popular vote
      - Arapahoe County had 6.7% (24,801 of 369,711) of total popular vote 
      
Denver County had the largest voter turnout when compared to the other two counties involved in the election. 

## Election Audit Results by Candidate

  - 369,711 total votes were casted in in Arapahoe, Denver, and Jefferson County in Colorado
  - The candidates were:
    - Charles Casper Stockham
    - Dianna DeGette
    - Raymon Anthony Doane
    
  -The candidate results were:
  
      - Charles Casper Stockham received 23.0% of the total popular vote (85,213 votes casted)
      - Diana DeGette received 73.8% of the total popular vote (272,892 votes casted)
      - Raymon Anthony Doane received 3.1% of the total popular vote (11,606 votes casted)
   
  The winner of the election was:
      - Diana DeGette who receieved 73.8% of the popular vote (272,892 votes out of 369,711)
      
 Below is the full summary of both county and candidate results
 
![Election_Results](https://user-images.githubusercontent.com/68922663/95687264-793bd700-0bd0-11eb-9fdc-6be03a6c8be8.png)

## Election Audit Summary
This script can be used for every future election in not only this Colorado congressional district, but all congressional districts across the United States. All that would have to be updated is the dataset (or .csv file) that we are using to determine the winner of the election. When this is updated at the beginning of the script, the new dataset will be incorporated to this script and results can be found quickly with precision. We may want to modify the script if we want additional analysis. For example, we could include an audit for each town involved in the election and thus, additonal code would need to be added similarly to how we analyzed results by county and candidate.
