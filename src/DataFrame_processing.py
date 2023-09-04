import pandas as pd
import random


def split_df(file, columns_of_df):
    # convert file in a DataFrame
    df = pd.read_excel(file)

    # save columns
    columns = df.columns[:3]

    # Calculate the number of smallest DataFrames you need
    number_of_df = len(df.columns) // columns_of_df

    # List to store the smaller DataFrames
    df_list = []

    # Split the main DataFrame into smaller DataFrames
    for i in range(number_of_df):
        start = i * columns_of_df
        end = start + columns_of_df
        new_df = df.iloc[:, start:end]
        
        # Rename columns with sequential numbers starting from 0
        new_df.columns = range(columns_of_df)
        
        # Append the new DataFrame to the list
        df_list.append(new_df)

    # return list of new df and head columns
    return df_list, columns

def processing_df(df_list, index_list, columns):

    new_df = pd.DataFrame()

    # Iterate through the random indices in the index_list
    for random_id in index_list:
        # Generate a random DataFrame index
        random_df = random.randint(0, len(df_list) - 1)

        # Check if the random_id is within the valid row range for the selected DataFrame
        if random_id < len(df_list[random_df]):
            # Extract the row from the selected DataFrame
            row_x = df_list[random_df].iloc[random_id]

            # Concatenate the row to the new DataFrame
            new_df = pd.concat([new_df, pd.DataFrame([row_x])], ignore_index=True)


    new_df.columns = columns # copy colums header in new df

    return new_df  # Return the new data frame