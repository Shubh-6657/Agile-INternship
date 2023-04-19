import pandas as pd

# Load the input data for statements and reasons into a Pandas DataFrame
df = pd.read_csv('input.csv')

# Create a new column 'team' by extracting the team name from the 'name' column
df['team'] = df['name'].apply(lambda x: x.split()[0])

# Calculate the average number of statements and reasons for each team
team_avg = df.groupby('team').mean()[['total_statements', 'total_reasons']]

# Calculate the team ranks based on the average number of statements
team_avg['team_rank'] = team_avg['total_statements'].rank(method='min', ascending=False).astype(int)

# Sort the teams based on the team rank
team_avg = team_avg.sort_values(by='team_rank')

# Rename the columns to match the output table
team_avg = team_avg.rename(columns={'total_statements': 'Average Statements', 'total_reasons': 'Average Reasons'})

# Print the output table
print('Team Rank\tThinking Teams Leaderboard\tAverage Statements\tAverage Reasons')
for i, row in team_avg.iterrows():
    print(f"{row['team_rank']}\t\t{i}\t\t\t{row['Average Statements']:.2f}\t\t\t{row['Average Reasons']:.2f}")
