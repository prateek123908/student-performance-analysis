import pandas as pd

# Module 1: Data Loading

def load_and_inspect_data(file_path):
#  Read the CSV file using Pandas.
   df=pd.read_csv(file_path)
#  Display the first five records.
   print("First five rows:\n",df.head(5).to_string(index=False))
#  Display the last five records.
   print("Last five rows:\n",df.tail(5).to_string(index=False))
#  Print the shape of the dataset.
   print("Dataset shape:\n",df.shape)
#  Print column names.
   print("Columns:\n",df.columns)
#  Display data types of each column.
   print("Data types:\n",df.dtypes)

# Module 2: Data Inspection
# Find missing values.
   print("Missing values:\n",df.isnull().sum())
# Find duplicate records.
   print("Duplicate records:\n",df.duplicated().sum())
# Display descriptive statistics.
   print("Descriptive statistics:\n",df.describe())
# Check memory usage.
   print("Memory usage:\n",df.memory_usage(deep=True))
# Display summary information.
   print("Summary Information:\n")
   df.info(memory_usage='deep')
   return df