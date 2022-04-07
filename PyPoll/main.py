import pandas as pd

# Read csv file as a data frame
df = pd.read_csv('Resources/election_data.csv')

# Get the total number of votes
Total_Votes = df.shape[0]

# The percentage of votes each candidate won
Percent = df['Candidate'].value_counts(normalize = True)*100

# The Total votes each candidate won
Candidate_Votes = df['Candidate'].value_counts()

# Winner of the election based on popular vote
# first get the max value in Percent (Percent is series)
# Then find the max value and get the index of it
Max = Percent.max()
Winner = Percent[Percent == Max].index[0]

# Writing results into a txt file
txt_path = 'analysis/results.txt'

with open (txt_path, 'w') as file:
    file.write ("Election Results \n" + 
               "-------------------------\n"+
               "Total Votes: " + str(Total_Votes) + "\n" + 
                "-------------------------\n" + 
                str(Percent.index[0]) + ": " + str(Percent[0]) + "%" + "(" + str(Candidate_Votes[0]) + ")\n" +
                 str(Percent.index[1]) + ": " + str(Percent[1]) + "%" + "(" + str(Candidate_Votes[1]) + ")\n" +
                 str(Percent.index[2]) + ": " + str(Percent[2]) + "%" + "(" + str(Candidate_Votes[2]) + ")\n" +
                "-------------------------\n" + 
                "Winner: " + str(Winner))