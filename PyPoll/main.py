# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# CSV FILE ASSUMPTIONS:
# Ballot IDs are unique integers
# County and Candidate are strings

# import os for filepaths, csv
import os
import csv

# constants for readability
BALLOT_COL = 0
COUNTY_COL = 1
CANDIDATE_COL = 2

# create path to csv
csvPath = os.path.join('Resources', 'election_data.csv')
resultsFile = open('results.txt', 'w', encoding='utf-8')

# open file for reading
with open(csvPath) as csvFile:
    # create reader with "," delimiter
    csvReader = csv.reader(csvFile, delimiter=',')
    # eat the header
    csvHeader = next(csvReader)

    #initialize trackers
    totalVotes = 0
    candidateVotes = {}

    for row in csvReader:
        # if the key for current data row does not exist in candidateVotes, add a count of 1
        if not candidateVotes.get(row[CANDIDATE_COL]):
            candidateVotes[row[CANDIDATE_COL]] = 1
        # else add 1 to the count
        else:
            candidateVotes[row[CANDIDATE_COL]] += 1
        # increment total votes
        totalVotes += 1

    # print results
    print("Election Results\n-------------------------")
    print(f"Total Votes: {totalVotes}\n-------------------------")

    # write results to file
    resultsFile.write("Election Results\n-------------------------\n")
    resultsFile.write(f"Total Votes: {totalVotes}\n-------------------------\n")

    # track winner
    winner = ""
    winnerPercent = 0.0
    # for each candidate/vote pair in dictionary
    for candidate, votes in candidateVotes.items():
        # calculate percent of votes for candidate
        percentTotal = (float(votes)/totalVotes) * 100
        # print out candidate and write to file
        print(f"{candidate}: {percentTotal:.3f}% ({votes})")
        resultsFile.write(f"{candidate}: {percentTotal:.3f}% ({votes})\n")
        # if winner is empty, this is the first row. set values accordingly
        if not winner:
            winner = candidate
            winnerPercent = percentTotal
        # if current percentTotal greater than winner, set new winner
        elif percentTotal > winnerPercent:
            winner = candidate
            winnerPercent = percentTotal
    print(f"-------------------------\nWinner: {winner}\n-------------------------")
    resultsFile.write(f"-------------------------\nWinner: {winner}\n-------------------------\n")

resultsFile.close()