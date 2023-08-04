import os
import csv
from collections import defaultdict
vote_counts = defaultdict(int)
file_path = os.path.join("..","GitHub","Module3-Challenge-Python","PyPoll","Resources","election_data.csv")
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