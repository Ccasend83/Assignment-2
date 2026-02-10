import pandas as pd

# load the dataset into a DataFrame
df = pd.read_csv('student.csv')

# filter students based on the three criteria
# conditions: studytime >= 3, internet == 1, and absences <= 5
filtered_df = df[
    (df['studytime'] >= 3) &
    (df['internet'] == 1) &
    (df['absences'] <= 5)
]

# save the filtered data to high_engagement.csv
filtered_df.to_csv('high_engagement.csv', index=False)

# calculate results
num_students = len(filtered_df)

avg_grade = filtered_df['grade'].mean()

# print the output
print(f"Number of students saved: {num_students}")
print(f"Average grade: {avg_grade:.2f}")