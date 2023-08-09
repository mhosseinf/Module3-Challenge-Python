import os
import csv
from collections import defaultdict
vote_counts = defaultdict(int)
Winner_count=0
file_path = os.path.join("Resources","election_data.csv")
with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    total_lines = len(list(csv_reader))
with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    for row in csv_reader:
            candidate = row[2]  # Assuming Candidate is at index 1 (0-indexed)

            # Update the vote count for the candidate
            vote_counts[candidate] += 1

# Print the vote counts for each candidate
print(f"Total Votes: {total_lines}" )
print("Vote counts for each candidate:")
for candidate, count in vote_counts.items():
    vote_percent=float(count/total_lines)
    print(f"{candidate}: {round((vote_percent)*100,3)}% ({count})  votes")
for candidate, count in vote_counts.items():
    if count>Winner_count:
          Winner=candidate
          Winner_count=count
print(f"Winner: {Winner}")
file_path2 = os.path.join("PyPoll-Outputs","PyPollresults.txt")
Poll_result = list(("Election Results","----------------------------",f"Total Votes: {total_lines}","----------------------------"))
winner_result = list(("----------------------------",f"Winner: {Winner}","----------------------------"))
with open(file_path2, 'w') as file:
        for item in Poll_result:
            file.write(str(item) + '\n')
        for candidate, count in vote_counts.items():
            vote_percent=float(count/total_lines)
            file.write(f"{candidate}: {round((vote_percent)*100,3)}% ({count})  votes"+'\n')
        for item in winner_result:
            file.write(str(item) + '\n')