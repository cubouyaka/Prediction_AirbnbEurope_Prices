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


# Load the data into a DataFrame
directory = 'airbnb'
df = load_data(directory)

# Examine the features of the dataset
print(df.head())
print(df.info())
print(df.describe())
