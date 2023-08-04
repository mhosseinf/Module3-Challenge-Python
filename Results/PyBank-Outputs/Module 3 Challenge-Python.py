import os
import csv
sum_column_2 = 0
file_path = os.path.join("..","GitHub","Module3-Challenge-Python","Pybank","Resources","budget_data.csv")
previous_value = None
change_sum = 0
count = 0
greatest_change=0
with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    total_lines = len(list(csv_reader))
with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        column_2_Value=int(row[1])
        sum_column_2+=column_2_Value
        # print(row[1])
        if previous_value is not None:
            change_sum += column_2_Value - previous_value
            count+=1
            # print(change_sum)
            # print(column_2_Value)
            current_change = change_sum       
            if current_change > greatest_change:
                greatest_change = current_change
        previous_value = column_2_Value
if count>0:
    average_change=change_sum/count
else:
    average_change=0
        

print("Total number of lines in the CSV file:", total_lines)
print("Net total amount of Profit/Losses is:", sum_column_2)
print("changes in Profit/Losses over the entire period:", average_change)
print("Greatest Increase in Profits:", greatest_change)