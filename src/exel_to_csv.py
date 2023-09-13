import os
from pathlib import Path

from DataFrame_processing import processing_df, split_df
from str import add_random_string

# Get the current script's directory path
BASE_DIR = Path(__file__).resolve().parent

# Construct the path to the Excel file within your project
file = os.path.join(BASE_DIR, "exel/exel_file.xlsx")
out = os.path.join(BASE_DIR, "out/random_exam.xlsx")

# Split the Excel file into a list of DataFrames and retrieve column names
df_list, columns = split_df(file, 3)

for i in range(5):

    ## ///////////////////////// ##
    # Create a list of unique random numbers between 0 and 49 (for random_ids)
    #random_ids = random.sample(range(50), min(49, len(df_list) * 50))

    # Create a list of unique random numbers between 50 and 70 (for random_ids2)
    #random_ids = random_ids + random.sample(range(50, 71), min(20, len(df_list) * 20))

    # Create a list of unique random numbers between 70 and 100 (for random_ids3)
    #random_ids = random_ids + random.sample(range(70, 101), min(31, len(df_list) * 31))
    ## ///////////////////////// ##

    # Create a list of numbers between 0 and 100
    random_ids = list(range(101))

    # Process the DataFrames using the random IDs and columns
    new_exam_df = processing_df(df_list, random_ids, columns)

    # Save the DataFrame to an Excel file
    new_exam_df.to_excel(add_random_string(file_path=out, length=10), index=False)