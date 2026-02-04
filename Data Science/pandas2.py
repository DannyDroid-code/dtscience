
import pandas as pd

data = pd.read_csv("titanic.csv")
print(data.head(10))

# Get the particular column out of a condition
# adult_names = data.loc[data["Age"] > 18, "Name"]
# print(adult_names)

# #Slicing - Same as numpy 2D slicing
# # The first index is for rows and the second is for columns, follows the same syntax as range function
# print(data.iloc[9:25, 2:5])
# print(data["Name"])
# Changing the value in the dataset
# Specify the number of rows and the particular column to change
# data.iloc[0:3, 3] = "Pulkit Chawla"
# print(data["Name"])

# # Save the data to local to verify changes
# data.to_csv("changedData.csv")

# Creating a new column in the dataFrame
# data["Test"] = data["Fare"] + 2
# data["Test2"] = data["Fare"] * data["Pclass"] # Any mathematical operation could be considered

# # Renaming the column names
# data_renamed = data.rename(
#     columns = {
#         "Pclass": "Passenger Class",
#         "Sibsp": "Sibling"
#     }
# )

# print(data_renamed.info())

# # Performing mathematical operation on multiple columns together
# print(data["Age"].mean())

# print(data[["Age", "Fare"]].mean())

# print(data.agg({
#     "Age": ["min", "max", "median"],
#     "Fare": ["min", "max", "median"]
# }))

# # Group by data categorically

# print(data[["Sex", "Age"]].groupby("Sex").mean())

# print(data.groupby("Sex")["Age"].mean())

# # # Task - Get the mean ticket price for each of sex and cabin class combination
# print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

# # Get the count of rows in each category
# print(data["Pclass"].value_counts())

# print(data.groupby("Pclass")["Pclass"].count())

# # Sorting the data
sorted =data.sort_values(by = "Age",ascending=False)
print(sorted.head(10))
print(data[["Name", "Age"]].head(10))
print(data.head(10))
data.sort_values(by = ["Pclass", "Age"], ascending = False)
print(data.head(10))

# # Operations on Text Data
data["NameLowercase"] = data["Name"].str.lower()
# #Other Examples to be shown
data["Name"].str.split(",")
data["Surname"] = data["Name"].str.split(" ").str.get(0)
data["Sex_short"] = data["Sex"].replace({"male": "M", "female": "F"})

