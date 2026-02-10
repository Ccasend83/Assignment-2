import pandas as pd

# load the dataset into a pandas
df_crime = pd.read_csv('crime.csv')

# create a new column called 'risk'
# default everything to "LowCrime"
df_crime['risk'] = 'LowCrime'

# if ViolentCrimesPerPop >= 0.50, set risk to "High-Crime"
df_crime.loc[df_crime['ViolentCrimesPerPop'] >= 0.50, 'risk'] = 'High-Crime'

# group the data by the 'risk' column
# for each group, calculate the average value of 'PctUnemployed'
summary = df_crime.groupby('risk')['PctUnemployed'].mean().reset_index()

# print the average unemployment rate in a clear format
# i use .iterrows to loop through each row in the pandas dataframe
print("Average Unemployment Rate by Crime Risk Level:")
for index, row in summary.iterrows():
    print(f"{row['risk']}: {row['PctUnemployed']:.2f}%")