import os
import csv
sum_column_3 = 0
#C:\Users\mh30f\OneDrive\Documents\GitHub\Module3-Challenge-Python\PyBank\Resources
#file_path = os.path.join("..","..","..","..","..","C:","Users","mh30f","OneDrive","Documents","GitHub","Module3-Challenge-Python","Pybank","Resources","budget_data.csv")
file_path = os.path.join("..","GitHub","Module3-Challenge-Python","Pybank","Resources","budget_data.csv")

with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    total_lines = len(list(csv_reader))
with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        column_3_Value=int(row[1])
        sum_column_3+=column_3_Value
        # print(row[1])


print("Total number of lines in the CSV file:", total_lines)
print("Net total amount of Profit/Losses is:", sum_column_3)