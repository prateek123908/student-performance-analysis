# Student Performance Data Handling and Analysis System

## Note:
- Output files are included in this repository as part of the **college academic submission requirement**
- In real-world industry projects, such generated files are usually excluded using `.gitignore`
- This project focuses on demonstrating data handling, transformation, and analysis using Pandas

## Project Description

This project is a Student Performance Data Handling and Analysis System. It was made using Python and Pandas.

The main goal of this project is to take student data from a CSV file make sure the data is correct add columns to show how well the students did look at the student performance and make reports.

---

## Objectives

- We need to load the student performance data and look at it

- We have to clean the data by fixing wrong values

- We need to change the data by adding grades and results and scores

- We have to look at how well all the students did

- We need to make CSV files for reports

---

## Technologies Used

- Python

- Pandas

- Git and GitHub

---

## Project Folder Structure

Student_Data_Project/

│

├── data/

│ └── student_dataset_v2.csv

│

├── output/

│ ├── cleaned_data.csv

│ ├── toppers.csv

│ ├── failed_students.csv

| ├── high_study_hours.csv

| ├── low_attendance.csv

│ └── report.csv

│

├── src/

│ ├── load_data.py

│ ├── clean_data.py

│ ├── transform.py

│ ├── analyse.py

│ └── report.py

├── main.py

└── README.md

---

## Project Workflow

1. **Data Loading**

It reads the CSV file

It shows information about the dataset

2. **Data Cleaning**

It removes records

It fixes missing values

It checks if the marks and attendance and study hours are correct

3. **Data Transformation**

It gives grades like A or B or C or D or F

It says if the student passed or failed

It calculates a performance score

It makes datasets with just the students we want to look at

4. **Data Analysis**

It calculates the marks and the highest and lowest marks

It looks at the attendance and study hour statistics

5. **Report Generation**

It makes a summary report in CSV format, for the Student Performance Data Handling and Analysis System