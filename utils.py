import os
import numpy as np
import pandas as pd


def load_data(path_to_directory):
    """ Load all cities data from path_to_directory into a DataFrame returned
    Args:
        path_to_directory: a String. The path to the directory where all .csv files are.
    Returns:
        A DataFrame df containing all the data.
    """
    dataframes = []
    # Loop through each file in the directory
    for filename in os.listdir(path_to_directory):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Load the CSV file into a dataframe
            df = pd.read_csv(os.path.join(path_to_directory, filename))
            # Add the city from the file name to the dataframe
            df["city"] = filename.split('_', 1)[0]
            # Add a bool weekdays from the file name to the dataframe
            if filename.split('_', 1)[1] == "weekdays.csv":
                df["weekdays"] = True
            elif filename.split('_', 1)[1] == "weekends.csv":
                df["weekdays"] = False
            # Append the dataframe to a list of dataframes
            dataframes.append(df)
    # Concatenate all the dataframes into one
    combined_df = pd.concat(dataframes, ignore_index=True)

    return combined_df


def handling_categorical_data(df, column_name):
    """Handling Categorical Data by replacing df[column_name] values by an associate index,
        returning this DataFrame modified and the Label encoding (unique integer value to each category)
        as a dictionary 'indexes'
    Args:
        df: a DataFrame. The DataFrame we want to modify.
        column_name: a string. The name of the df column we want to refactor.
    Returns:
        A pair (df, indexes) containing the DataFrame 'df' modified, and a Dictionary 'indexes' containing values of
        df[column_name] and its index (the new value in df[column_name]).
    """
    current_i = 0
    indexes = {}
    for value in df[column_name].unique():
        indexes[value] = current_i
        current_i += 1
    df[column_name] = df[column_name].map(indexes)
    return df, indexes


def handling_categorical_datas(df):
    """Handling Categorical Data of all the columns in the DataFrame 'df'
    Args:
        df: a DataFrame. The DataFrame we want to modify.
    Returns:
        A pair (df, indexes) containing the DataFrame 'df' modified now containing only integer values to each category,
        and a set
    """
    indexes = {}
    for column in df.columns:
        if len(df[column]) > 0 and not np.isreal(df[column][0]):  # check if it doesn't contain numerical values
            df, indexes[column] = handling_categorical_data(df, column)  # convert values in numerical values

    return df, indexes

