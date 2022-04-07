import os
import csv
import pandas as pd

csvpath = os.path.join('Resources','budget_data.csv')

# Save the csv file as a Data Frame 
df = pd.read_csv(csvpath)

# Calculate the Total months
Total_Months = df.shape[0]

# Calculate the net total amount of profit/losses over the entire period
Total = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
# Create a changes list to contain the values that calculated from each month.
changes = []
changes.append(None)
for i in range(0,85):
    changes.append(df['Profit/Losses'][i+1] - df['Profit/Losses'][i])
    
# Store the values into the data frame
df['Changes'] = changes

# Calculate the average of Changes
Average_Changes = df['Changes'].mean()

# Calculate the greatest increase in profits
Greatest_Increase = df['Changes'].max()
Greatest_Increase_Date = df.loc[df['Changes'] == Greatest_Increase,'Date'].values[0]

# Calculate the greatest decrease in profits
Greatest_Decrease = df['Changes'].min()
Greatest_Decrease_Date = df.loc[df['Changes'] == Greatest_Decrease,'Date'].values[0]

# Set path for results text file
txt_path = 'analysis/results.txt'

# Write changes to the txt file
with open (txt_path, 'w') as file:
    file.write ("Financial Analysis\n" +
                "----------------------------\n" +
                "Total Months:" + str(Total_Months)+"\n" +
                "Total: "+ str(Total)+"\n" +
                "Average Change: $" + str(Average_Changes)+"\n" +
                "Greatest Increase in Profits: " + str(Greatest_Increase_Date) + " "+ str(Greatest_Increase) +"\n" +
                "Greatest Decrease in Profits: " + str(Greatest_Decrease_Date) + " "+ str(Greatest_Decrease))
    file.close()
    
    