import pandas as pd

# load the dataset into a DataFrame
student_time_dataframe = pd.read_csv('student.csv')

# filter students based on the three criteria
# conditions: studytime >= 3, internet == 1, and absences <= 5
filtered_student_time_dataframe = student_time_dataframe[
    (student_time_dataframe['studytime'] >= 3) &
    (student_time_dataframe['internet'] == 1) &
    (student_time_dataframe['absences'] <= 5)
]

# save the filtered data to high_engagement.csv
filtered_student_time_dataframe.to_csv('high_engagement.csv', index=False)

# calculate results
# total number of students
number_students_of_total_students = len(filtered_student_time_dataframe)

# get the average/mean of the students
average_grades_of_students = filtered_student_time_dataframe['grade'].mean()

# print the output
print(f"Number of students saved: {number_students_of_total_students}")
print(f"Average grade: {average_grades_of_students:.2f}")