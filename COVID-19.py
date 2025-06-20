import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the COVID-19 dataset
df = pd.read_csv("C:\\Users\\radhi\\Desktop\\COVID-19 Dataset.csv")

# Step 2: Initial inspection
print(df)                     # Print full dataset (for debugging, usually not used in large datasets)
print(df.shape)               # Show the number of rows and columns
print(df.head(10))            # Show first 10 rows for a quick look
print(df.info())              # Overview: column types, nulls, memory
print(df.info())              # Duplicate call — can be removed (redundant)

# Step 3: Check for missing values in all columns
print(df.isnull().sum())      # Shows count of nulls per column

# Step 4: Drop rows with any null values (optional: not always ideal)
df.dropna(inplace=True)       # Removes rows where *any* column is NaN
print(df.shape)               # New shape after dropping nulls

# Step 5: Show column names for reference
print(df.columns)

# Step 6: Define the countries you want to analyze
countries = ['India', 'United Kingdom', 'Brazil', 'Germany']
print(countries)

# Step 7: Filter the dataset for only the selected countries
df_countries = df[df['Country/Region'].isin(countries)]
print(df_countries)

# Step 8: (Optional) Create a new dataframe with only rows where WHO Region is not missing
df1 = df[df['WHO Region'].notna()]
print(df1)

# Step 9: Replace any remaining missing values with 0 — usually for numeric columns
# Note: Inplace returns None, so don’t print it directly
df.fillna(0, inplace=True)

# Final check (optional): Confirm all NaN are handled
print(df.isnull().sum())

#Group
top_countries = df.groupby('Country/Region')['Confirmed'].sum().reset_index()
print("\nGrouped countries:\n", top_countries)
print()

# Sort and print top 10

top_countries = top_countries.sort_values(by='Confirmed', ascending=False).head(10)
print("\nTop 10 countries:\n", top_countries)
top_countries = df.groupby('Country/Region')[['Confirmed', 'Deaths']].sum().reset_index()
top_countries = top_countries.sort_values(by='Deaths', ascending=False).head(10)
print(top_countries)
print()

# Now group by Country/Region and sum New cases
top_countries = df.groupby('Country/Region')[['New cases']].sum().reset_index()
# Sort and pick top 10
top_countries = top_countries.sort_values(by='New cases', ascending=False).head(10)
# Print result
print(top_countries)
print()

# Now group by Country/Region and sum New deaths
top_countries = df.groupby('Country/Region')[['New deaths']].sum().reset_index()
# Sort and pick top 10
top_countries = top_countries.sort_values(by='New deaths', ascending=False).head(10)
# Print result
print("New deaths",top_countries)
print( )


# Now group by Country/Region and sum Confirmed last week
top_countries = df.groupby('Country/Region')[['Confirmed last week']].sum().reset_index()

# Sort and pick top 10
top_countries = top_countries.sort_values(by='Confirmed last week', ascending=False).head(10)

# Print result
print("Confirmed last week:", top_countries)




#Trend Visualization 
# Set figure size
sns.set(rc={'figure.figsize': (15, 5)})

# Plot bar chart
sns.barplot(data=top_countries, x='Country/Region', y='Confirmed')

# Set title and labels
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Country/Region")
plt.ylabel("Confirmed Cases")

 # Set figure size
sns.set(rc={'figure.figsize': (15, 5)})

# Plot bar chart
sns.lineplot(data=top_countries, x='Country/Region', y='Confirmed')

# Set title and labels
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Country/Region")
plt.ylabel("Confirmed Cases")

# Rotate x-axis labels
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

# plot Top 10 Countries by Deaths:
sns.set(rc={'figure.figsize': (15, 5)})
 
sns.lineplot(data=top_countries, x='Country/Region', y='Deaths')
plt.title("Top 10 Countries by COVID-19 Deaths")
plt.xlabel("Country/Region")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#plot Tpo 10 New Cases
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=top_countries, x='Country/Region', y='New cases', palette='Blues')
plt.title("Top 10 Countries by New COVID-19 Cases")
plt.xlabel("Country/Region")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#plot top 10 new deaths
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=top_countries, x='Country/Region', y='New deaths', palette='Reds')
plt.title("Top 10 Countries by New COVID-19 Deaths")
plt.xlabel("Country/Region")
plt.ylabel("New Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#top 10 Confirmed last week
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=top_countries, x='Country/Region', y='Confirmed last week', palette='Blues',legend=False)
plt.title("Top 10 Countries by Confirmed COVID-19 Cases Last Week")
plt.xlabel("Country/Region")
plt.ylabel("Confirmed Cases Last Week")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
