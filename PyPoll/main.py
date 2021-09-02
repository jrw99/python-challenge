import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "election_data_analysis.txt")
totalVoteCount = 0

    
# =============================================================================
# Function that takes in a known dicitonairy for election ananlysis and prints 
# the results to screen    
# =============================================================================
def printToScreen(results_dict):
    print("")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {results_dict['totalVotes']}")
    print("----------------------------")
    for candidate in results_dict['candidateList']:
        print(f"{candidate['name']}: {candidate['percentage']}% ({candidate['votes']})")
    print("----------------------------")
    print(f"Winner: {results_dict['name']}")
    print("----------------------------")


# =============================================================================
# Function that takes in a known dictionairy for election ananlysis and prints
# the results to a file
# =============================================================================
def printToFile(output_file, results_dict):

    #  Open the output file and write the results
    with open(output_file, "w", newline="") as outfile:
        
        outfile.write("\n")
        outfile.write("Election Results\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Votes: {results_dict['totalVotes']}\n")
        outfile.write("----------------------------\n")
        for candidate in results_dict['candidateList']:
            outfile.write(f"{candidate['name']}: {candidate['percentage']}% ({candidate['votes']})\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Winner: {results_dict['name']}\n")
        outfile.write("----------------------------\n")


# =============================================================================
# Function that takes in candidate votes and total vote count to calculate 
# vote percentage
# =============================================================================
def getPercentage(candidateVotes, totalVotes):
    percentage =  '{:.3f}'.format(round(((candidateVotes / totalVotes) * 100), 3))   
    return percentage
    

with open(election_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')       
    csv_header = next(csvreader) 
    
    # we can save some memory by just working with the candidate column
    # based on the structure of the data
    election_list = list(row[2] for row in csvreader)
   

# determine how many votes are in the set. Voter ID should be unique 
# and therefore each row constitues a single vote so a straight count
# of the rows would be the total vote count
totalVoteCount = len(election_list)


# get a unique list of the candidates
candidates_set = set(election_list)

# use the unique list to get their respective votes
candidate_dict = {}
for candidate in candidates_set:
   candidate_dict.update({candidate:election_list.count(candidate)})

# Now that we have a list of candidates with there vote counts, who had the 
# most votes...
candidateWithLargestNumberOfVotes = max(candidate_dict, key=candidate_dict.get)  

# calculate the percenatage each candidates votes were of the total vote count
# and store with their record
candidate_list = []
for candidate, votecount in candidate_dict.items():    
    candidate_list.append({'name':candidate, 'votes':votecount, 'percentage':getPercentage(votecount, totalVoteCount)})

# amalgamate the results for rendering
results_dict = {'totalVotes': totalVoteCount, 
                'candidateList': sorted(candidate_list, key=lambda k: k['votes'], reverse=True),
                'name': candidateWithLargestNumberOfVotes}


# =============================================================================
# Print the results to both the screen and a file
# =============================================================================
printToScreen(results_dict)

printToFile(output_file, results_dict)


    
        