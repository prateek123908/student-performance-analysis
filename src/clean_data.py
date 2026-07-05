import pandas as pd

# Module 3: Data Cleaning
def cleaned_data(df):
    # Perform appropriate cleaning operations such as:
    # • Remove duplicate records.
    df=df.drop_duplicates()
    # Handle missing values.
    marks_average=df['Marks'].mean()
    df['Marks']=df['Marks'].fillna(marks_average)
    df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())
    df['StudyHours'] = df['StudyHours'].fillna(df['StudyHours'].mean())
    # Remove invalid entries.
    # Validate attendance values.
    df=df[(df['Attendance'] >= 0) & (df['Attendance'] <= 100)]
    # Validate study hours.
    df=df[(df['StudyHours'] >= 0)]
    # Validate marks.
    df=df[(df['Marks'] >= 0) & (df['Marks'] <= 100)]
    return df
