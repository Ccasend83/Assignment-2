import pandas as pd

# load the dataset
student_grade_dataframe = pd.read_csv('student.csv')

# create the grade_band column
# i used .loc to access each individual row and columns in the pandas dataframe
# initialize the column with Medium as the default
student_grade_dataframe['grade_band'] = 'Medium'

# assign Low where grade <= 9
student_grade_dataframe.loc[student_grade_dataframe['grade'] <= 9, 'grade_band'] = 'Low'

# assign High where grade >= 15
student_grade_dataframe.loc[student_grade_dataframe['grade'] >= 15, 'grade_band'] = 'High'

# generate the grouped summary table
organized_summary_table = student_grade_dataframe.groupby('grade_band').agg(
    number_of_students=('grade', 'count'),
    average_absences=('absences', 'mean'),
    percentage_with_internet=('internet', 'mean')
).reset_index()

# convert internet ratio to a percentage
organized_summary_table['percentage_with_internet'] = ((organized_summary_table['percentage_with_internet'] * 100).round(2).astype(str)
                                             +'%')

# save the table
organized_summary_table.to_csv('student_bands.csv', index=False)

print(organized_summary_table)