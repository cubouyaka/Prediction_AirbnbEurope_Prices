import os
import pandas as pd


# Load all cities data from path_to_directory into a DataFrame returned
def load_data(path_to_directory):
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
        df[column_name] and its index (the new value in df[column_name]
    """
    current_i = 0
    indexes = {}
    for value in df[column_name].unique():
        indexes[value] = current_i
        current_i += 1
    df[column_name] = df[column_name].map(indexes)
    return df, indexes


# Load the data into a DataFrame
directory = 'airbnb'
df = load_data(directory)

# Examine the features of the dataset
# print(df['room_type'].head(20))
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())  # number of null values