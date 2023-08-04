import os
import csv
sum_column_2 = 0
file_path = os.path.join("..","GitHub","Module3-Challenge-Python","Pybank","Resources","budget_data.csv")
previous_value = 0
change_sum = 0
count = 0
greatest_Increase=0
greatest_Decrease=0
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
        if previous_value != 0:
            change_sum += column_2_Value - previous_value
            count+=1
            # print(change_sum)
            # print(column_2_Value)
        current_change = column_2_Value - previous_value
        if current_change > greatest_Increase:
            greatest_Increase = current_change
            greatest_Increase_month=row[0]
        
        if current_change < greatest_Decrease:
            greatest_Decrease = current_change
            greatest_Decrease_month=row[0]

        previous_value = column_2_Value
if count>0:
    average_change=change_sum/count
else:
    average_change=0
        

print("Total number of lines in the CSV file:", total_lines)
print("Net total amount of Profit/Losses is:", sum_column_2)
print("changes in Profit/Losses over the entire period:", round(average_change,2))
print(f"Greatest Increase in Profits: {greatest_Increase_month} {greatest_Increase}")
print(f"Greatest Decrease in Profits: {greatest_Decrease_month} {greatest_Decrease}")
result_dict = {
    f"Total number of lines in the CSV file: {total_lines}":total_lines,
    f"Net total amount of Profit/Losses is:${sum_column_2}":sum_column_2,
    f"changes in Profit/Losses over the entire period: ${round(average_change,2)}":average_change,
    f"Greatest Increase in Profits: {greatest_Increase_month}: ${greatest_Increase}":greatest_Increase,
    f"Greatest Decrease in Profits: {greatest_Decrease_month}: ${greatest_Decrease}":greatest_Decrease
}

file_path2 = os.path.join("..","GitHub","Module3-Challenge-Python","Results","PyBank-Outputs","PyBankresults.txt")
with open(file_path2, 'w') as file:
    for result in result_dict:
        file.write(result + '\n')