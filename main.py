import sys
sys.path.append('.')

from src.load_data import load_and_inspect_data
from src.clean_data import cleaned_data
from src.transform import transform_data
from src.analyse import analyse_data
from src.report import generate_report

raw_df=load_and_inspect_data("data/student_dataset_v2.csv")

cleaned_df=cleaned_data(raw_df)
cleaned_df.to_csv("output/cleaned_data.csv", index=False)

transformed_df=transform_data(cleaned_df)

stats_result=analyse_data(transformed_df)

report_df=generate_report(transformed_df,stats_result)
report_df.to_csv("output/report.csv", index=False)