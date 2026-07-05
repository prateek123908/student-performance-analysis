import pandas as pd

# Module 4: Data Transformation
# # Create the following new columns:
# Grade: Assign grades according to marks.
# Example: A B C D F
# Result : Pass  Fail
# Performance Score
# Create a custom performance score using Marks, Attendance, and Study Hours
def calculate_grade(Marks):
    if Marks >= 90:
        return 'A'
    elif Marks >= 80:
        return 'B'
    elif Marks >= 70:
        return 'C'
    elif Marks >= 60:
        return 'D'
    else:
        return 'F'
    
def transform_data(df):
    df['Grade']=df['Marks'].apply(calculate_grade)
    df['Result']=df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    df['PerformanceScore']=(df['Marks']*0.6)+(df['Attendance']*0.3)+(df['StudyHours']*0.1)

# Module 5: Data Filtering
# Generate separate datasets for:
# Top-performing students
# Failed students
# Students with attendance below 75%
# Students studying more than 8 hours
# Save the filtered datasets as separate CSV files
    toppers=df[df['Grade']=='A']
    toppers.to_csv("output/toppers.csv", index=False)
    failed_students=df[df['Result']=='Fail']
    failed_students.to_csv("output/failed_students.csv", index=False)
    low_attendance=df[df['Attendance']<75]
    low_attendance.to_csv("output/low_attendance.csv", index=False)
    high_study_hours=df[df['StudyHours']>8]
    high_study_hours.to_csv("output/high_study_hours.csv", index=False)
    return df
    