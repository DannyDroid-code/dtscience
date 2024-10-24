#a
import pandas as pd

# Load the dataset
df = pd.read_csv("vgsales.csv")

# Fill missing values in "Year" with the mode or median
df['Year'] = df['Year'].fillna(df['Year'].mode()[0])

# Fill missing values in "Publisher" with the mode (most frequent publisher)
df['Publisher'] = df['Publisher'].fillna(df['Publisher'].mode()[0])

# Display the updated dataset to check for missing values
print(df.isnull().sum())


#b
# Convert "Year" column to integer type
df['Year'] = df['Year'].astype(int)

# Check the data types of the columns
print(df.dtypes)


#c

# Group by publisher and sum North America sales
na_sales_by_publisher = df.groupby('Publisher')['NA_Sales'].sum()

# Sort in descending order and get the top 10 publishers
top_10_na_publishers = na_sales_by_publisher.sort_values(ascending=False).head(10)

# Display the top 10 publishers
print(top_10_na_publishers)



#d

import matplotlib.pyplot as plt

# Group by publisher and sum sales for each region and globally
sales_by_publisher = df.groupby('Publisher')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

# Create a line plot for each sales region and globally
plt.figure(figsize=(12, 8))

# Line plot for NA, EU, JP, Other, and Global sales
for region in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']:
    sales_by_publisher[region].sort_values(ascending=False).head(10).plot(label=region)

# Customize the plot
plt.title('Publisher-wise Total Units Sold in Different Regions')
plt.xlabel('Publisher')
plt.ylabel('Total Units Sold (in millions)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


#e

# Find the publisher with the maximum global sales
max_global_sales = sales_by_publisher['Global_Sales'].idxmax()
max_global_sales_value = sales_by_publisher['Global_Sales'].max()

print(f"The publisher with the most global sales is {max_global_sales}, with {max_global_sales_value:.2f} million units sold.")
