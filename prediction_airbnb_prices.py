from utils import load_data, handling_categorical_datas


# Load the data into a DataFrame
directory = 'airbnb'
data = load_data(directory)

# # Examine the features of the dataset
# print(data['room_type'].head(20))
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())  # number of null values

# Handling Categorical Data in data and storing the associate indexes
data, indexes = handling_categorical_datas(data)
