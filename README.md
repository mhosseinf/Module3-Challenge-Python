# Bootcamp: WAUS-VIRT-DATA-PT-07-2023-U-LOLC-MTTH
#Module3-Challenge-Python

#PyBank includes 2 folders and 1 Python script:
1-Resource folder contains a financial dataset, The associated file is called budget_data.csv
2-PyBank-Outputs folder contains a text file that has the results from the Python script.

#PyPoll includes 2 folders and 1 Python script:
1-Resource folder contains a set of poll data. The associated file is called election_data.csv
2-PyPoll-Outputs folder contains a text file that has the results from the Python script.


#I created a folder named "Results/PyPoll-Outputs" to store the initial results. However, I realised that results need to be located in the same folder where the dataset is located, so I rearranged the files and moved scripts for both PayBank and PyPoll into the same folder. I feel like this action deleted the history of the evolution of the scripts and the step-by-step improvements made to each script. So I thought maybe good to explain why that is.

#PyBank Scripts structure:
It reads the financial data from a CSV file. Used the os. path.join() function to handle file paths
then open the file as a CSV file and read it. 
1-len() function used to count the total number of months included in the dataset
2-in a for loop, it checks the profit/losses in column 2 and uses a conditional statement to calculate below:
2-1) First-if, calculates the change in column 2 values(profit/losses) between the current and previous rows and accumulates it using change_sum += column_2_Value - previous_value. It also keeps track of the count of changes.
2-2) Second/third if, updates the variables greatest_Increase and greatest_Decrease based on the current change in column 2 values and updates the corresponding months if applicable.

3-if-condition out of the for loop, calculate the average of changes

4- the last part of the script prints the results in terminal
5-Also, export a text file with the results.