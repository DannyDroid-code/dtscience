import pandas as pd
#a)
# Load the dataset
df = pd.read_csv("LifeExpectancy.csv")

# Rename columns by stripping spaces
df.columns = df.columns.str.strip()

# Display the column names
print(df.columns)


#b
# Check missing values in each column
missing_values = df.isnull().sum()

# Display columns that have missing values
missing_columns = missing_values[missing_values > 0]
print(missing_columns)


#c
# Set the threshold to 15% of the rows
threshold = len(df) * 0.15

# Drop columns with more than 15% missing values
df = df.dropna(thresh=len(df) - threshold, axis=1)

# Display the remaining columns
print(df.columns)

#d
# Fill missing values with the median for each column
df = df.fillna(df.median())

# Check if any missing values remain
print(df.isnull().sum())


#e
import matplotlib.pyplot as plt

# Filter data between 2000 and 2015
df_filtered = df[(df['Year'] >= 2000) & (df['Year'] <= 2015)]

# Group by year and calculate the average life expectancy
avg_life_expectancy = df_filtered.groupby('Year')['Life expectancy'].mean()

# Plot the bar chart
plt.figure(figsize=(10, 6))
avg_life_expectancy.plot(kind='bar', color='skyblue')
plt.title('Global Average Life Expectancy (2000-2015)')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.show()


#f
# Find the year with maximum average life expectancy
max_year = avg_life_expectancy.idxmax()
max_value = avg_life_expectancy.max()

print(f"The maximum average life expectancy was in {max_year}, with a value of {max_value:.2f} years.")


#g
# Group by year and status, then calculate the mean life expectancy
life_expectancy_status = df_filtered.groupby(['Year', 'Status'])['Life expectancy'].mean().unstack()

# Plot the bar chart
life_expectancy_status.plot(kind='bar', figsize=(12, 8), width=0.8)
plt.title('Yearly Life Expectancy of Developed and Developing Countries (2000-2015)')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.xticks(rotation=45)
plt.show()
