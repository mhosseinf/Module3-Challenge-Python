import os
import csv
sum_column_2 = 0
file_path = os.path.join("..","GitHub","Module3-Challenge-Python","PyPoll","Resources","election_data.csv")
with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    total_lines = len(list(csv_reader))
# with open(file_path, 'r', newline='') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     next(csv_reader)
#     for row in csv_reader:


print("Total number of lines in the CSV file:", total_lines)