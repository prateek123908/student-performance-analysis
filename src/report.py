import pandas as pd

def generate_report(df, analysis):
    report = {
        'Total Students': len(df),
        'Passed Students': (df['Result'] == 'Pass').sum(),
        'Failed Students': (df['Result'] == 'Fail').sum(),
        'Highest Marks': analysis['Highest Marks'],
        'Lowest Marks': analysis['Lowest Marks'],
        'Average Marks': analysis['Average Marks'],
        'Average Attendance': analysis['Average Attendance']
    }

    report_df = pd.DataFrame(report.items(), columns=['Metric', 'Value'])
    return report_df