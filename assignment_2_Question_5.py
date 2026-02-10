import pandas as pd

# load the dataset
df = pd.read_csv('student.csv')

# create the grade_band column
# initialize the column with Medium as the default
df['grade_band'] = 'Medium'

# assign Low where grade <= 9
df.loc[df['grade'] <= 9, 'grade_band'] = 'Low'

# assign High where grade >= 15
df.loc[df['grade'] >= 15, 'grade_band'] = 'High'

# generate the grouped summary table
summary_table = df.groupby('grade_band').agg(
    number_of_students=('grade', 'count'),
    average_absences=('absences', 'mean'),
    percentage_with_internet=('internet', 'mean')
).reset_index()

# convert internet ratio to a percentage
summary_table['percentage_with_internet'] = ((summary_table['percentage_with_internet'] * 100).round(2).astype(str)
                                             +'%')

# save the table
summary_table.to_csv('student_bands.csv', index=False)

print(summary_table)