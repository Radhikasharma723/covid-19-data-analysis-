import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\radhi\\Desktop\\COVID-19 Dataset.csv")
# Basic inspection
print(df.shape)  # Show the number of rows and columns
print(df.columns)  # Show column names for reference
print(df.info())   # Overview: column types, nulls, memory
print(df.head())   # Show first 10 rows for a quick look

# Check for missing values
print()
print("Missing values per column:\n", df.isnull().sum())  # Shows count of nulls per column

# Drop rows with any missing data (optional)
df.dropna(inplace=True)

# Replace remaining missing values (if any) with 0
df.fillna(0, inplace=True)

# Final check
print()
print("After cleaning:\n", df.isnull().sum())

# Analyze Specific Countries 

countries = ['India', 'United Kingdom', 'Brazil', 'Germany']
df_selected = df[df['Country/Region'].isin(countries)]
print()
print(df_selected.head())


# Total Confirmed Cases
confirmed_df = df.groupby('Country/Region')['Confirmed'].sum().reset_index()
confirmed_df = confirmed_df.sort_values(by='Confirmed', ascending=False).head(10)
print("🔹 Top 10 Countries by Total Confirmed Cases:\n", confirmed_df, "\n")

# Total Deaths
deaths_df = df.groupby('Country/Region')['Deaths'].sum().reset_index()
deaths_df = deaths_df.sort_values(by='Deaths', ascending=False).head(10)
print("🔹 Top 10 Countries by Total Deaths:\n", deaths_df, "\n")

# New Cases
new_cases_df = df.groupby('Country/Region')['New cases'].sum().reset_index()
new_cases_df = new_cases_df.sort_values(by='New cases', ascending=False).head(10)
print("🔹 Top 10 Countries by New Cases:\n", new_cases_df, "\n")


# New Deaths
new_deaths_df = df.groupby('Country/Region')['New deaths'].sum().reset_index()
new_deaths_df = new_deaths_df.sort_values(by='New deaths', ascending=False).head(10)
print("🔹 Top 10 Countries by New Deaths:\n", new_deaths_df, "\n")


# Confirmed Last Week
last_week_df = df.groupby('Country/Region')['Confirmed last week'].sum().reset_index()
last_week_df = last_week_df.sort_values(by='Confirmed last week', ascending=False).head(10)
print("🔹 Top 10 Countries by Confirmed Cases Last Week:\n", last_week_df, "\n")

# Visualization: Trend Charts

#Top 10 Countries - Confirmed Cases
sns.barplot(data=confirmed_df, x='Country/Region', y='Confirmed', palette='Blues_d')
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Countries - Deaths
sns.barplot(data=deaths_df, x='Country/Region', y='Deaths', palette='Reds')
plt.title("Top 10 Countries by COVID-19 Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Countries - New Cases
sns.barplot(data=new_cases_df, x='Country/Region', y='New cases', palette='Purples')
plt.title("Top 10 Countries by New COVID-19 Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Countries - New Deaths
sns.barplot(data=new_deaths_df, x='Country/Region', y='New deaths', palette='Reds_r')
plt.title("Top 10 Countries by New COVID-19 Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Confirmed Last Week
sns.barplot(data=last_week_df, x='Country/Region', y='Confirmed last week', palette='Greens')
plt.title("Top 10 Countries by Confirmed COVID-19 Cases Last Week")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Advanced: Line Plot for Trends Over Time (if dataset includes a date column)
# Optional: If your dataset has a 'Date' column
df['Date'] = pd.to_datetime(df['Date'])

# Plot daily confirmed cases for selected countries
for country in countrie:
    country_df = df[df['Country/Region'] == country]
    plt.plot(country_df['Date'], country_df['Confirmed'], label=country)

plt.title('Confirmed Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.legend()
plt.tight_layout()
plt.show()

#Final Touch: Save Cleaned Data (optional)
columns = df.columns.tolist()
print("Available columns:\n", columns)
 



