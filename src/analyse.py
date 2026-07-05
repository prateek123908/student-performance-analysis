import pandas as pd

# Module 6: Data Analysis
def analyse_data(df):
# Perform the following analysis:
# Average Marks
    avg_marks = df['Marks'].mean()
# Highest Marks
    highest_marks = df['Marks'].max()
# Lowest Marks
    lowest_marks = df['Marks'].min()
# Average Attendance
    avg_attendance = df['Attendance'].mean()
# Average Study Hours
    avg_study_hours = df['StudyHours'].mean()
# Pass Percentage
    pass_percentage = (df['Result'] == 'Pass').mean() * 100
# Fail Percentage
    fail_percentage = (df['Result'] == 'Fail').mean() * 100
# Grade Distribution
    grade_distribution = df['Grade'].value_counts()
    
    return{
    'Average Marks': avg_marks,
    'Highest Marks': highest_marks,
    'Lowest Marks': lowest_marks,
    'Average Attendance': avg_attendance,
    'Average Study Hours': avg_study_hours,
    'Pass Percentage': pass_percentage,
    'Fail Percentage': fail_percentage,
    'Grade Distribution': grade_distribution
   }